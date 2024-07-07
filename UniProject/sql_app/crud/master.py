from sqlalchemy.orm import Session

from models import master as models
from schemas import master as schemas

def get_master(db: Session, lid: str):
    return db.query(models.master).filter(models.master.lid == lid).first()

def create_master(db: Session, pmaster: schemas.pmaster):
    db_master = models.master(
        lid=pmaster.lid,
        fname=pmaster.fname,
        lname=pmaster.lname,
        id=pmaster.id,
        department=pmaster.department,
        major=pmaster.major,
        birth=pmaster.birth,
        borncity=pmaster.borncity,
        address=pmaster.address,
        postalcode=pmaster.postalcode,
        cphone=pmaster.cphone,
        hphone=pmaster.hphone,
        lcourseids=pmaster.lcourseids)
    db.add(db_master)
    db.commit()
    db.refresh(db_master)
    return db_master

def delete_master(db: Session, lid: str):
    master = db.query(models.master).filter(models.master.lid == lid).first()
    if master:
        db.delete(master)
        db.commit()
        return True

def update_master(db: Session, lid: str, updated_data: schemas.masterupdate):
    db_master = db.query(models.master).filter(models.master.lid == lid).first()
    if db_master:
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_master, field, value)
        db.commit()
        db.refresh(db_master)
        return db_master
    return None

















# def get_stu(db: Session, stid: str):
#     return db.query(models.prstu).filter(models.prstu.stid == stid).first()

# def create_student(db: Session, prstu: schemas.prstu):
#     db_student=models.student(stid=prstu.stid,fname=prstu.fname,lname=prstu.lname,father=prstu.father,
#                               birth=prstu.birth,ids=prstu.ids,borncity=prstu.borncity,address=prstu.address,
#                               postalcode=prstu.postalcode,cphone=prstu.cphone,
#                               hphone=prstu.hphone,department=prstu.department,major=prstu.major,
#                               married=prstu.married,id=prstu.id,scourseids=prstu.scourseids,lids=prstu.lids)
#     db.add(db_student)
#     db.commit()
#     db.refresh(db_student)
#     return

# def delete_student(db: Session, stid: str):
#     student = db.query(models.prstu).filter(models.prstu.stid == stid).first()
#     if student:
#         db.delete(student)
#         db.commit()
#         return True

# class va:
#     def check_course_in_db(db: Session, Course_id: int) -> bool:
#         return db.query(models.Course).filter(models.Course.id == Course_id).first() is not None

# def course_db(db: Session, course_id: int) -> bool:
#     try:
#         course = db.query(models.Course).filter(models.Course.id == course_id).first()
#         return course is not None
#     except Exception as e:
#         print(f"Error occurred while checking course in database: {str(e)}")
#         return False