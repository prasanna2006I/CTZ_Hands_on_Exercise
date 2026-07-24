from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "mysql+pymysql://root:password@localhost/college_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100))
    head_of_dept = Column(String(100))
    budget = Column(Float)

    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollment_year = Column(Integer)

    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="students")


Base.metadata.create_all(engine)