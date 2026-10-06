from fastapi import APIRouter

from database import student_collection
from models import Student_model

student_router=APIRouter(prefix="/student",tags=["student"])

#localhost:8000/student/addstudent=>add
@student_router.post("/addStudent")
def addStudent(stu:Student_model):
    result=student_collection.insert_one(stu.model_dump())
    return "student inserted success"

#localhost:8000/student/getstudent=>get
@student_router.get("/getStudent")
def getStudent():
    return "get student method called"

#localhost:8000/student/updatestudent=>put
@student_router.put("/updateStudent")
def updateStudent():
    return "update student method called"

#localhost:8000/student/deletestudent=> delete
@student_router.delete("/deleteStudent")
def deleteStudent():
    return "delete student method called"

