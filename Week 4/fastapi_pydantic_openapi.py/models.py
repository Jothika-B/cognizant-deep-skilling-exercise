from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John")
    age: int = Field(..., ge=18, le=60, example=21)
    course: str = Field(..., example="Computer Science")
