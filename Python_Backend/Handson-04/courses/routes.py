from flask import (
    Blueprint,
    jsonify,
    request
)

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []


@courses_bp.route(
    "/",
    methods=["GET"]
)
def get_courses():
    return jsonify(courses)
@courses_bp.route(
    "/<int:id>",
    methods=["GET"]
)
def get_course(id):

    if id >= len(courses):

        return (
            jsonify(
                {
                    "error":
                    "Course not found"
                }
            ),
            404
        )

    return jsonify(
        courses[id]
    )

@courses_bp.route(
    "/",
    methods=["POST"]
)
def create_course():

    data = request.get_json()

    if not data:
        return (
            jsonify(
                {
                    "error":
                    "JSON required"
                }
            ),
            400
        )

    required = [
        "name",
        "code",
        "credits"
    ]

    for field in required:

        if field not in data:

            return (
                jsonify(
                    {
                        "error":
                        f"{field} required"
                    }
                ),
                400
            )

    courses.append(data)

    return (
        jsonify(data),
        201
    )

@courses_bp.route(
    "/<int:id>",
    methods=["DELETE"]
)
def delete_course(id):

    if id >= len(courses):

        return (
            jsonify(
                {
                    "error":
                    "Course not found"
                }
            ),
            404
        )

    deleted = courses.pop(id)

    return jsonify(
        deleted
    )