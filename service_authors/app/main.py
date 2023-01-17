from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry import trace
from fastapi import FastAPI, HTTPException

from app.author import Author, CreateAuthorModel
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

authors: list[Author] = []


def add_new_author(context: CreateAuthorModel):
    id_ = len(authors)
    authors.append(Author(
        str(id_),
        context.name,
        context.username,
        context.email,
        context.address))
    return id_


app = FastAPI()

##########
# Jaeger

resource = Resource(attributes={
    SERVICE_NAME: "service_authors"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

#
##########

##########
# Prometheus


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


#
##########


@app.get("/api/authors")
async def get_authors():
    return authors


@app.post("/api/add-author")
async def add_author(content: CreateAuthorModel):
    add_new_author(content)
    return authors[-1]


@app.get("/api/author/{id_}")
async def get_author_by_id(id_: str):
    result = [item for item in authors if item.id == id_]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Author not found")


@app.get("/__health")
async def check_service():
    return {"status": "alive"}
