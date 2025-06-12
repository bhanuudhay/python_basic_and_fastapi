from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
import models
from passlib.context import CryptContext
from database import get_db

def get_userr(db : Session = Depends(get_db)):
    user = db.query(models.User).all()
    if not user:
        return {'error': 'No user found'}
    return user

def get_user_id(id , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail={'error': f"user with id {id} not found"})
    return user

pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_user(request , db : Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    user  = models.User(username=request.username, email=request.email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user