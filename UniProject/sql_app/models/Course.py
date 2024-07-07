from sqlalchemy import Column, Integer, String
from schemas import Course as schemas
from database import Base


class Course(Base):
    __tablename__ = "Course"

    CID = Column(String,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(Integer)