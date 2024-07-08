from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class student(BaseModel):
    stid: str
    fname: str
    lname : str
    father : str

class Config:
    orm_mode = True

class prstu(student):    
    birth : str
    ids : str  #سریال شناسنامه
    borncity : str
    address : str
    postalcode : str
    cphone: str
    hphone: str      #تلفن ثابت
    department : str
    major : str    #رشته
    married : str
    id : str
    scourseids : str
    lids :  str   # اساتید

class studentupdate(BaseModel):
    stid:Optional[str]=None
    fname: Optional[str] = None
    lname: Optional[str] = None
    father: Optional[str] = None
    birth:Optional[str]=None
    ids: Optional[str] = None
    borncity: Optional[str] = None
    address: Optional[str] = None
    postalcode:Optional[str]=None
    cphone: Optional[str] = None
    hphone: Optional[str] = None
    department: Optional[str] = None
    major:Optional[str]=None
    married: Optional[str] = None
    id: Optional[str] = None
    scourseids: Optional[str] = None
    lids: Optional[str] = None
