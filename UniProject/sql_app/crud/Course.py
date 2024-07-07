from sqlalchemy.orm import Session

from models import Course as models
from schemas import Course as schemas


def get_Course(db: Session, Course_id: int):
    return db.query(models.Course).filter(models.Course.CID == Course_id).first()

def create_Course(db: Session, Course: schemas.Course):
    db_Course=models.Course(CID=Course.CID,
                            CName=Course.CName,
                            Department=Course.Department,
                            Credit=Course.Credit)
    db.add(db_Course)
    db.commit()
    db.refresh(db_Course)
    return db_Course

def delete_Course(db: Session, Course_id: int):
    Course = db.query(models.Course).filter(models.Course.CID == Course_id).first()
    if Course:
        db.delete(Course)
        db.commit()
        return True
    
def update_Course(db: Session, Course_id: int, Course_update: schemas.CourseUpdate):
    Course = db.query(models.Course).filter(models.Course.CID == Course_id).first()
    if not Course:
        return None
    
    update_data = Course_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(Course, key, value)
    
    db.add(Course)
    db.commit()
    db.refresh(Course)
    return Course