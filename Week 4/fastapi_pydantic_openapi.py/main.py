from fastapi import FastAPI
from models import Student

app = FastAPI(
    title="Student API",
    description="FastAPI example using Pydantic models with automatic OpenAPI documentation.",
    version="1.0.0"
)

students = []

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.post("/students/")
def add_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }

@app.get("/students/")
def get_students():
    return students
