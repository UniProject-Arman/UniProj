import uvicorn
if __name__ == "__main__":
    uvicorn.run("config:app",host="0.0.0.0",port=8000,reload=True)

from models import Course,student,master
from database import engine

Course.Base.metadata.create_all(bind=engine)
student.Base.metadata.create_all(bind=engine)
master.Base.metadata.create_all(bind=engine)

