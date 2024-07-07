from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Course(BaseModel):
    CID: str
    CName: str
    Department : str
    Credit : int

class CourseUpdate(BaseModel):
    CID:Optional[str]=None
    CName: Optional[str] = None
    Department: Optional[str] = None
    Credit: Optional[int] = None