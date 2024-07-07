from sqlalchemy.orm import Session

from models import student as models
from schemas import student as schemas

def get_stu(db: Session, stid: str):
    return db.query(models.student).filter(models.student.stid == stid).first()

def create_student(db: Session, prstu: schemas.prstu):
    db_student = models.student(
        stid=prstu.stid,
        fname=prstu.fname,
        lname=prstu.lname,
        father=prstu.father,
        birth=prstu.birth,
        ids=prstu.ids,
        borncity=prstu.borncity,
        address=prstu.address,
        postalcode=prstu.postalcode,
        cphone=prstu.cphone,
        hphone=prstu.hphone,
        department=prstu.department,
        major=prstu.major,
        married=prstu.married,
        id=prstu.id,
        scourseids=prstu.scourseids,
        lids=prstu.lids)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, stid: str):
    student = db.query(models.student).filter(models.student.stid == stid).first()
    if student:
        db.delete(student)
        db.commit()
        return True

def update_student(db: Session, stid: str, updated_data: schemas.studentupdate):
    db_student = db.query(models.student).filter(models.student.stid == stid).first()
    if db_student:
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_student, field, value)
        db.commit()
        db.refresh(db_student)
        return db_student
    return None