from fastapi import APIRouter
staff_router=APIRouter(prefix="/staff",tags=["staff"])

#localhost:8000/staff/addstaff=>add
@staff_router.post("addStaff")
def addStaff():
    return "add staff method called"

#localhost:8000/staff/getstaff=>get
@staff_router.get("/getStaff")
def getStaff():
    return "get staff method called"

#localhost:8000/staff/updatestaff=>put
@staff_router.put("/updateStaff")
def updateStaff():
    return "update staff method called"

#localhost:8000/staff/deletestaff=> delete
@staff_router.delete("/deleteStaff")
def deleteStaff():
    return "delete staff method called"

