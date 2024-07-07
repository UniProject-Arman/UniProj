from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from crud import Course as crud
from datavalidation import valcourse
from schemas import Course as schemas
from models import Course as models
from dependencies import get_db
router=APIRouter()

@router.post("/CreateCourse/", response_model=schemas.Course)
def create_user(Course: schemas.Course, db: Session = Depends(get_db)):
    valcourse.cid_check(Course.CID)
    valcourse.cname_check(Course.CName)
    valcourse.dep_check(Course.Department)
    valcourse.credit_check(Course.Credit)
    db_Course = crud.get_Course(db, Course_id=Course.CID)
    if db_Course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_Course(db=db, Course=Course)


@router.get("/GetCourse/{Course_id}", response_model=schemas.Course)
def read_Course(Course_id: int, db: Session = Depends(get_db)):
    db_Course = crud.get_Course(db, Course_id=Course_id)
    if db_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_Course


@router.delete("/DelCourse/{Course_id}")
def delete_Course(Course_id: int, db: Session = Depends(get_db)):
    success = crud.delete_Course(db, Course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"Course deleted successfully"}


@router.patch("/UpCourse/{Course_id}", response_model=schemas.CourseUpdate)
def update_Course(Course_id: int, Course_update: schemas.CourseUpdate, db: Session = Depends(get_db)):
    valcourse.cid_check(Course.CID)
    valcourse.cname_check(Course.CName)
    valcourse.dep_check(Course.Department)
    valcourse.credit_check(Course.Credit)
    Course = crud.get_Course(db, Course_id)
    if Course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_Course = crud.update_Course(db, Course_id, Course_update)
    if updated_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return updated_Course
