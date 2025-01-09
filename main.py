from fastapi import FastAPI
from fastapi.responses import  HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from backend.api.main_router import router
from backend.core.database.db_helper import db_helper
from backend.core.utils import iter_file
from backend.core.config import settings
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(application:FastAPI):
    yield
    await db_helper.close()

app=FastAPI(lifespan=lifespan)


app.mount('/frontend',StaticFiles(directory='frontend'),name='frontend')
app.mount('/media',StaticFiles(directory='media'),name='media')

@app.get("/")
def hello():
    return StreamingResponse(iter_file('frontend/html/a.html'),media_type='text/html')

app.include_router(router=router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']

    )

if __name__=="__main__":
    uvicorn.run("main:app",host=settings.run.host,port=settings.run.port)
