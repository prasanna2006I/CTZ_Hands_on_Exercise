from flask import Flask, request
import requests

app = Flask(__name__)

# Forward course requests to Course Service
@app.route("/api/courses/<path:path>", methods=["GET"])
def course_proxy(path):
    response = requests.get(
        f"http://127.0.0.1:5001/api/courses/{path}"
    )
    return response.text, response.status_code
@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def student_proxy(id):
    response = requests.post(
        f"http://127.0.0.1:5002/api/students/{id}/enroll",
        json=request.json
    )
    return response.text, response.status_code

if __name__ == "__main__":
    app.run(port=5000)