from fastapi import FastAPI
from models import Course

app = FastAPI()

courses = []


@app.get("/")
def home():

    return {
        "message":
        "Handson 08"
    }


@app.post("/api/courses/")
def create_course(
    course: Course
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
def get_courses():

    return courses


@app.get(
    "/api/courses/{course_id}"
)
def get_course(
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


@app.put(
    "/api/courses/{course_id}"
)
def update_course(
    course_id: int,
    course: Course
):

    for index, item in enumerate(
        courses
    ):

        if (
            item["id"]
            ==
            course_id
        ):

            updated = course.dict()

            updated["id"] = (
                course_id
            )

            courses[
                index
            ] = updated

            return updated

    return {
        "error":
        "Course not found"
    }


@app.delete(
    "/api/courses/{course_id}"
)
def delete_course(
    course_id: int
):

    for index, item in enumerate(
        courses
    ):

        if (
            item["id"]
            ==
            course_id
        ):

            return courses.pop(
                index
            )

    return {
        "error":
        "Course not found"
    }