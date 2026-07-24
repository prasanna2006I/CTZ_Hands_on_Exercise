from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):
    data = request.get_json()
    course_id = data["course_id"]

    try:
        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({"message": "Course not found"}), 404

        return jsonify({
            "message": f"Student {id} enrolled in Course {course_id}"
        }), 200
    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503

if __name__ == "__main__":
    app.run(port=5002)