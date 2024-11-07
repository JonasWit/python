from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello 2"}

@app.get("/posts")
def get_posts():
    return { "data": "posts"}
