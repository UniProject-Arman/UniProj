from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from schemas import student as schemas
from database import Base


class student(Base):
    __tablename__ = "student"

    stid =Column(String,primary_key=True)
    fname =Column(String)
    lname  =Column(String)
    father  =Column(String)   
    birth  =Column(String)
    ids  =Column(String)
    borncity  =Column(String)
    address=Column(String)
    postalcode  =Column(String)
    cphone =Column(String)
    hphone =Column(String)      
    department  =Column(String)
    major =Column(String)  
    married  =Column(String)
    id =Column(String)
    scourseids=Column(String)
    lids=Column(String)
