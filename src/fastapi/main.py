from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio

async def print_task(s): 
    while True:
        print('Hello from background')
        await asyncio.sleep(s)
             
@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(print_task(5))
    yield
    print('Shutting down...')
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return { "message": "Hello 2"}

@app.get("/posts")
async def get_posts():
    return { "data": "posts"}
