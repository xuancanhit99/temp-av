from fastapi import FastAPI
import pika

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "OK"}


@app.get("/add-job/{message}")
def add_job(message: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    connection.close()

    return {"send": message}
