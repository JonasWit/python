from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio

async def print_task(s): 
    while True:
        print('Hello from background')
        await asyncio.sleep(s)
             
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    asyncio.create_task(print_task(5))
    yield
    # Run on shutdown (if required)
    print('Shutting down...')
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return { "message": "Hello 2"}

@app.get("/posts")
async def get_posts():
    return { "data": "posts"}
