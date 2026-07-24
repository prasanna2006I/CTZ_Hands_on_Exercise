# Handson-08: CRUD Operations with FastAPI

## Objective

The objective of this hands-on is to build a RESTful API using FastAPI that performs complete CRUD (Create, Read, Update, Delete) operations for course management using in-memory data storage.

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
Handson-08/
│
├── .venv/
├── main.py
├── models.py
└── requirements.txt
```

---

## Installation

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

## Running the Application

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
  "message": "Handson 08"
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

---

### Update Course

**PUT /api/courses/{course_id}**

Example Request:

```json
{
  "name": "Advanced Python",
  "code": "PY201",
  "credits": 4
}
```

Response:

```json
{
  "id": 1,
  "name": "Advanced Python",
  "code": "PY201",
  "credits": 4
}
```

---

### Delete Course

**DELETE /api/courses/{course_id}**

Example:

```
DELETE /api/courses/1
```

Response:

```json
{
  "id": 1,
  "name": "Advanced Python",
  "code": "PY201",
  "credits": 4
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

- Create REST APIs using FastAPI
- Define request models with Pydantic
- Implement CRUD operations
- Use path parameters
- Return JSON responses
- Test APIs using Swagger UI and Postman

---

## Author

**Name:** PRASANNA I

**Course:** Python Backend Development

**Handson:** 08 – CRUD Operations using FastAPI
