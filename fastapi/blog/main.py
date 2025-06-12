from fastapi import FastAPI, Depends
import  models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

@app.post('/blog')
def create(request:Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

@app.get('/blog')
def all( db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id:int, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog