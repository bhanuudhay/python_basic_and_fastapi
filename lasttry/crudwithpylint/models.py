from database import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    roll_no = Column(Integer)
    # owner_id = Column(Integer , ForeignKey("users.id")) # ForeignKey is used to link the student to the user

    # owner = relationship("User" , back_populates="students") # back_populates is used to get the user from the student and student from the user

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    # students = relationship("Student" , back_populates="owner") # back_populates is used to get the user from the student and student from the user back_populates is used to get the user from the student and student from the user

