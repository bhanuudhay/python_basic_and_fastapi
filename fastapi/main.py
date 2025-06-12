from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() #instance of the fastapi class

#path
@app.get("/") #path and get is the operation on the path

#path operation function
def index():
    return {'data': 'Welcome to home page'}

#keep static method above the dynamic method
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

#this will give me list of all the blog but if i need one blog that
@app.get('/blogs')
def blog():
    return {'data': 'all blogs'}

#query parameters need to be passed in the function
@app.get('/blog')
#only get 10 published blog
def blog(limit:int = 10, published:bool = True , sort: Optional[str] = None): #default value is 10 and published is True
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} unpublished blogs from the database'}

#for dynamic routing we can use this {id}
@app.get('/blog/{id}')
#after getting the value dynamically we can use it in the function

def show(id : int): # by default it is string but we can change it to int and for string str 
    return {'data': id} 

@app.get('/blog/{id}/comment') # fast api is smart enough which is path parameter and what is query parameter 
def comments(id : int, limit:int):
    #fetch comment of the blog with id = id
    return limit
    return {'data':{'comment':{"1","2"}}}


@app.get('/about') #what matter the most is the decorator 
def about():
    return {'data' : "this is the about page "}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]



@app.post('/blog')
def create_blog(request:Blog ):
    return {'data': f'blog is created with title {request.title} and body {request.body} '} 
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app , host= "127.0.0.1",  port=9000)
