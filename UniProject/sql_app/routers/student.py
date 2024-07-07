from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import student as crud
from datavalidation import valstu
from schemas import student as schemas
from models import student as models
from dependencies import get_db

router=APIRouter()

@router.post("/createstudent/", response_model=schemas.student)
def create_student(prstu: schemas.prstu, db: Session = Depends(get_db)):

    valstu.stid_check(prstu.stid)
    valstu.fname_check(prstu.fname)
    valstu.lname_check(prstu.lname)
    valstu.fathername_check(prstu.father)
    valstu.birth_check(prstu.birth)
    valstu.ids_check(prstu.ids)
    valstu.born_check(prstu.borncity)
    valstu.address_check(prstu.address)
    valstu.postal_check(prstu.postalcode)
    valstu.cphone_check(prstu.cphone)
    valstu.hphone_check(prstu.hphone)
    valstu.dep_check(prstu.department)
    valstu.major_check(prstu.major)
    valstu.marrie_check(prstu.married)
    valstu.id_check(prstu.id)
    valstu.scid_check(prstu.scourseids)
    valstu.lid_check(prstu.lids)


    db_student = crud.get_stu(db, stid=prstu.stid)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exists")
    student = crud.create_student(db, prstu)
    return student

@router.get("/students/{stid}", response_model=schemas.student)
def read_student(stid: str, db: Session = Depends(get_db)):
    student = crud.get_stu(db, stid)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/delstu/{stid}")
def delete_student(stid: str, db: Session = Depends(get_db)):
    success = crud.delete_student(db, stid)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}
    
@router.patch("/updatestudent/{stid}", response_model=schemas.student)
def update_student(stid: str, prstu: schemas.studentupdate, db: Session = Depends(get_db)):
    valstu.stid_check(prstu.stid)
    valstu.fname_check(prstu.fname)
    valstu.lname_check(prstu.lname)
    valstu.fathername_check(prstu.father)
    valstu.birth_check(prstu.birth)
    valstu.ids_check(prstu.ids)
    valstu.born_check(prstu.borncity)
    valstu.address_check(prstu.address)
    valstu.postal_check(prstu.postalcode)
    valstu.cphone_check(prstu.cphone)
    valstu.hphone_check(prstu.hphone)
    valstu.dep_check(prstu.department)
    valstu.major_check(prstu.major)
    valstu.marrie_check(prstu.married)
    valstu.id_check(prstu.id)
    valstu.scid_check(prstu.scourseids)
    valstu.lid_check(prstu.lids)

    updated_student = crud.update_student(db=db, stid=stid, updated_data=prstu)
    if updated_student is None:
        raise HTTPException(status_code=404, detail=f"Student not found")
    return updated_student