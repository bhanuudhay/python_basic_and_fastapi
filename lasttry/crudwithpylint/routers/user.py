from fastapi import APIRouter, Depends, HTTPException, status, Response
from passlib.context import CryptContext
from schemas import User , showUser
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from repository.user import get_userr , get_user_id
import models
router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/' , status_code = status.HTTP_201_CREATED)
def create_user(request : User , db : Session = Depends(get_db)):
    return create_user(request , db)

@router.get('/' , response_model = List[showUser] , status_code = status.HTTP_200_OK)
def get_user(db : Session = Depends(get_db)):
    return get_userr(db)

@router.get('/{id}' , response_model = showUser , status_code = status.HTTP_200_OK)
def get_single_user(id , db : Session = Depends(get_db)):
    return get_user_id(id , db)