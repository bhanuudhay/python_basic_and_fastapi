from fastapi import Depends , HTTPException , status
from sqlalchemy.orm import Session
import models
from database import get_db
from schemas import Student
def get_all_students(db : Session = Depends(get_db)):
    students = db.query(models.Student).all()
    if not students:
        raise HTTPException(status_code=404, details="No student found")
    return students

def create_student(request ,db : Session = Depends(get_db) ):
    new_student = models.Student(name=request.name, age=request.age, roll_no=request.roll_no)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_single_student(id , response , db : Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f"student with id {id} not found"}
    return student

def delete_student(id , db : Session = Depends(get_db)):
    student  = db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session=False) #synchronize_session=False is used to avoid the error of session conflict
    db.commit()
    return {'data':f"student with id {id} deleted"}

def update_student(id , request , db : Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student.first():
       raise HTTPException(status_code=404, detail={'error': f"student with id {id} not found"})
        
    else:
        student.update(request.dict())
        db.commit()
    return "updated successfully"