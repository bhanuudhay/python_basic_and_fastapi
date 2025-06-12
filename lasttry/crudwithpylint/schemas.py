from pydantic import BaseModel

class ShowStudent(BaseModel):
    name: str
    age: int
    roll_no: int

    class Config:
        orm_mode = True 

class Student(BaseModel):  # this will create student = Student(name="Rahul", age=20, roll_no=101)

    name: str
    age: int 
    roll_no: int

class User(BaseModel):
    username: str
    email : str
    password : str

class showUser(BaseModel):
    username : str
    email : str
    id : int
    class Config():
        orm_mode = True

class ShowStudent(BaseModel):
    name : str
    age : int
    class Config(): # allow Pydantic to read data from SQLAlchemy objects
        orm_mode = True