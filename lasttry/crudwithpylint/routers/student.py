from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas import ShowStudent, Student    
from repository.student import get_all_students , create_student , get_single_student , delete_student , update_student

router = APIRouter(
    prefix='/student',
    tags=['student']
)

@router.post('/' , status_code = status.HTTP_201_CREATED)
def add_student(request: Student, db: Session = Depends(get_db)):
    return create_student(db , request)

@router.get('/', response_model=List[ShowStudent])
def get_students(db: Session = Depends(get_db)):
    return get_all_students(db)

@router.get('/{id}' , status_code = status.HTTP_200_OK ,  response_model=ShowStudent)
def getSingleStudent(id:int ,response : Response, db : Session = Depends(get_db) ):
    return get_single_student(id , response , db)

@router.delete('/{id}' , status_code = status.HTTP_204_NO_CONTENT)
def destroy(id , db : Session = Depends(get_db)):
   return delete_student(id , db)

@router.put('/{id}' , status_code = status.HTTP_202_ACCEPTED)
def update(id , request : Student , db : Session = Depends(get_db)): # request body is needed for schema validation 
    return update_student(id , request , db)