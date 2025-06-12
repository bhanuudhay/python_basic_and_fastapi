from typing import List
from fastapi import FastAPI,Depends, status , Response , HTTPException
from pydantic import BaseModel
import models
from database import engine , get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import uvicorn
from routers import student, user , authentication

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get('/' , tags=['home'])
def home():
    return {'data': 'Welcome to home page'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

