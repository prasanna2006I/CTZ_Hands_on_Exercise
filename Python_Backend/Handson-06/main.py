from fastapi import FastAPI
from schemas import (
    CourseCreate
)

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = []


@app.get("/")
def home():

    return {
        "message":
        "API running"
    }


@app.post(
    "/api/courses/"
)
async def create_course(
    course: CourseCreate
):

    data = course.dict()

    data["id"] = (
        len(courses) + 1
    )

    courses.append(
        data
    )
    return data
@app.get("/api/courses/")
async def get_courses():
    return courses


@app.get(
    "/api/courses/{course_id}"
)
async def get_course(
    course_id: int
):

    for course in courses:

        if (
            course["id"]
            ==
            course_id
        ):

            return course

    return {
        "error":
        "Course not found"
    }