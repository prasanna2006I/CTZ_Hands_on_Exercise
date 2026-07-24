# Handson-07: FastAPI CRUD API

## Objective

The objective of this hands-on is to develop a RESTful API using FastAPI that performs Create, Read, and Retrieve operations for course management using in-memory storage.

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

---

## Project Structure

```
Handson-07/
│
├── .venv/
├── main.py
├── models.py
└── requirements.txt
```

---

## Installation

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install fastapi uvicorn pydantic
```

---

## Running the Application

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

Application URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home

**GET /**

Returns a welcome message.

Response:

```json
{
  "message": "API running"
}
```

---

### Create Course

**POST /api/courses/**

Request Body:

```json
{
  "name": "Python",
  "code": "PY101",
  "credits": 3
}
```

Response:

```json
{
  "id": 1,
  "name": "Python",
  "code": "PY101",
  "credits": 3
}
```

---

### Get All Courses

**GET /api/courses/**

Response:

```json
[
  {
    "id": 1,
    "name": "Python",
    "code": "PY101",
    "credits": 3
  }
]
```

---

### Get Course by ID

**GET /api/courses/{course_id}**

Example:

```
GET /api/courses/1
```

Response:

```json
{
  "id": 1,
  "name": "Python",
  "code": "PY101",
  "credits": 3
}
```

If the course is not found:

```json
{
  "error": "Course not found"
}
```

---

## Testing the API

The API can be tested using:

- Swagger UI
- Postman

Swagger URL:

```
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

- Build REST APIs using FastAPI
- Create request models using Pydantic
- Implement Create and Read operations
- Use path parameters
- Return JSON responses
- Test APIs using Swagger UI and Postman

---

## Author

**Name:** PRASANNA I

**Course:** Python Backend Development

**Handson:** 07 – FastAPI CRUD API
