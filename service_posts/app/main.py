from fastapi import FastAPI, HTTPException
from app.post import Post
posts: list[Post] = [
    Post(
        "1",
        "1",
        "The Coming Population Crash",
        "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"),
    Post("2",
         "1",
         "An Essay on the Principle of Population",
         "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla")
]


app = FastAPI()


@app.get("/api/posts")
async def get_posts():
    return posts


@app.get("/api/post/{id_}")
async def get_post_by_id(id_: str):
    result = [item for item in posts if item.id == id_]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Post not found")
