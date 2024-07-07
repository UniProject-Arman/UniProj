from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class master(BaseModel):
    lid : str
    fname : str
    lname  : str
    id : str
    
class Config:
    orm_mode = True

class pmaster(master):
    department  : str
    major : str   
    birth  : str
    borncity  : str
    address: str
    postalcode  : str
    cphone : str
    hphone : str      
    lcourseids: str



class masterupdate(BaseModel):
    lid : Optional[str] = None
    fname : Optional[str] = None
    lname  : Optional[str] = None
    id : Optional[str] = None
    department  : Optional[str] = None
    major : Optional[str] = None   
    birth  : Optional[str] = None
    borncity  : Optional[str] = None
    address: Optional[str] = None
    postalcode  : Optional[str] = None
    cphone : Optional[str] = None
    hphone : Optional[str] = None      
    lcourseids: Optional[str] = None
