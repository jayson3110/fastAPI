from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')

def index(limit=10, published: bool = True, sort:Optional[str] = None):

    if published:
        return {'data':f' {limit} published blogs list from the db '}

    else:
        return {'data':f' {limit} blogs list from the db '}


@app.get('/blog/unpublished')

def unpublished():
    return {'data': 'Unpublished Blogs'}




@app.get('/blog/{id}')

def show(id: int):
    #fetch blog with id = id
    return {'data': id}




@app.get('/blog/{id}/comments')

def comments(id, limit=10):

    return {'data': {'1', '2'}}




class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')

def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request}"}