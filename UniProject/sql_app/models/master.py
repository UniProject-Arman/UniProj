from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from schemas import master as schemas
from database import Base


class master(Base):
    __tablename__ = "master"

    lid =Column(String,primary_key=True)
    fname =Column(String)
    lname  =Column(String)
    id =Column(String)
    department  =Column(String)
    major =Column(String)   
    birth  =Column(String)
    borncity  =Column(String)
    address=Column(String)
    postalcode  =Column(String)
    cphone =Column(String)
    hphone =Column(String)      
    lcourseids=Column(String)