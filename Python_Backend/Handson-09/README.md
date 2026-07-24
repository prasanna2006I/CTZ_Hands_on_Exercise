# Handson-09: JWT Authentication with FastAPI

## Objective

The objective of this hands-on is to implement JWT (JSON Web Token) authentication in a FastAPI application. The API allows users to generate a JWT token and access a protected endpoint using that token.

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- python-jose (JWT)
- Postman / Swagger UI

---

## Project Structure

```
Handson-09/
│
├── .venv/
├── auth.py
├── main.py
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

### 3. Install Required Packages

```bash
pip install fastapi uvicorn python-jose passlib python-multipart
```

---

## Running the Application

```bash
uvicorn main:app --reload
```

Application runs at:

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
  "message": "JWT API"
}
```

---

### Login

**POST /login**

Generates a JWT token.

Response:

```json
{
  "token": "<jwt_token>"
}
```

---

### Protected Route

**GET /profile**

Requires JWT authentication.

Authorization Header:

```
Bearer <jwt_token>
```

Response:

```json
{
  "message": "Access granted",
  "user": {
    "user": "admin"
  }
}
```

---

## Testing with Postman

### Login

Method:

```
POST
```

URL:

```
http://127.0.0.1:8000/login
```

Copy the JWT token from the response.

### Access Protected Endpoint

Method:

```
GET
```

URL:

```
http://127.0.0.1:8000/profile
```

Authorization:

- Type: Bearer Token
- Paste the JWT token

Click **Send**.

---

## Learning Outcomes

- Understand JWT Authentication
- Generate JWT tokens
- Verify JWT tokens
- Protect API endpoints
- Test APIs using Swagger and Postman
- Implement Authorization headers in FastAPI
---
## Author
**Name:** PRASANNA I

**Course:** Python Backend Development

**Handson:** 09 – JWT Authentication using FastAPI
