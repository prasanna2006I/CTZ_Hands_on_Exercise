from fastapi import FastAPI
from models import Course

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = []


@app.get("/")
def home():
    return {
        "message": "API running"
    }


@app.post("/api/courses/")
def create_course(course: Course):

    data = course.dict()

    data["id"] = len(courses) + 1

    courses.append(data)

    return data


@app.get("/api/courses/")
def get_courses():

    return courses


@app.get("/api/courses/{course_id}")
def get_course(course_id: int):

    for course in courses:

        if course["id"] == course_id:
            return course

    return {
        "error": "Course not found"
    }