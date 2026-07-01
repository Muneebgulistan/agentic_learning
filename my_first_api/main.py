from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to Day 2!"}

# Path Parameter Example
@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "status": "Student Found"
    }

# Query Parameter Example
@app.get("/search")
def search_student(name: str):
    return {
        "student_name": name
    }