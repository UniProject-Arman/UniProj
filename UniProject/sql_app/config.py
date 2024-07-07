from fastapi import FastAPI
from routers import Course,student,master


app = FastAPI()
app.include_router(Course.router, tags=["Courses"])
app.include_router(student.router, tags=["Students"])
app.include_router(master.router, tags=["Masters"])