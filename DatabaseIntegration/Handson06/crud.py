from models import SessionLocal, Student, Department

session = SessionLocal()

new_student = Student(
    first_name="Prasanna",
    last_name="I",
    email="prasanna@gmail.com",
    enrollment_year=2024,
    department_id=1
)

session.add(new_student)
session.commit()

students = session.query(Student).all()

print("Students")

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name,
        student.email
    )

student = session.query(Student).filter_by(first_name="Prasanna").first()

if student:
    student.enrollment_year = 2025
    session.commit()

student = session.query(Student).filter_by(first_name="Prasanna").first()

if student:
    session.delete(student)
    session.commit()

session.close()