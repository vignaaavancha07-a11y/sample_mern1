from fastapi import FastAPI
app=FastAPI()

@app.get("/getStudents")
def getStudents():
    return "get student method called"