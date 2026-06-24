from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection
engine = create_engine("sqlite:///students.db")

# Base class
Base = declarative_base()

# Create Model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

# Create table
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()


# CREATE
def create_student(name, age, department):
    student = Student(
        name=name,
        age=age,
        department=department
    )
    session.add(student)
    session.commit()
    print("Student added successfully")


# READ
def read_students():
    students = session.query(Student).all()

    print("\nStudent Records")
    for s in students:
        print(
            f"ID: {s.id}, "
            f"Name: {s.name}, "
            f"Age: {s.age}, "
            f"Department: {s.department}"
        )


# UPDATE
def update_student(student_id, new_department):
    student = session.query(Student).filter_by(
        id=student_id
    ).first()

    if student:
        student.department = new_department
        session.commit()
        print("Student updated")
    else:
        print("Student not found")


# DELETE
def delete_student(student_id):
    student = session.query(Student).filter_by(
        id=student_id
    ).first()

    if student:
        session.delete(student)
        session.commit()
        print("Student deleted")
    else:
        print("Student not found")


# Execute CRUD
create_student("Jothika", 20, "CSE")
create_student("Arun", 21, "ECE")

read_students()

update_student(1, "AI & DS")

read_students()

delete_student(2)

read_students()
