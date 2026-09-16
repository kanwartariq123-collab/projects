from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    dad_name = Column(String)
    father_profession = Column(String)
    mother_name = Column(String)
    contact = Column(String)
    emergency_phone = Column(String)
    course = Column(String)
    hobby = Column(String)
    weight = Column(String)
    height = Column(String)
    dob = Column(String)
    blood_group = Column(String)
    admission_date = Column(String)