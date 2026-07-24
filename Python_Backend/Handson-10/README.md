# Hands-On 10: Microservices Architecture

## Objective

This hands-on demonstrates how to decompose a monolithic Course Management System into independent microservices, implement inter-service communication, and use an API Gateway.

---

# Service Decomposition

| Service Name | Responsibility | Endpoints | Database |
|--------------|---------------|-----------|----------|
| Course Service | Manage courses | /api/courses | course.db |
| Student Service | Manage students and enrollments | /api/students | student.db |
| Auth Service | User registration and login | /api/auth | auth.db |
| Notification Service | Send email notifications | /api/notifications | notification.db |

---

# Services Created

## 1. Course Service

- Runs on Port **5001**
- Manages course information
- Provides course details using:
  - GET /api/courses/<id>

---

## 2. Student Service

- Runs on Port **5002**
- Handles student enrollment
- Before enrolling a student, it calls the Course Service to verify the course exists.

Endpoint:
- POST /api/students/<id>/enroll

---

## 3. API Gateway

- Runs on Port **5000**
- Receives client requests
- Routes requests to the appropriate microservice

Routing:

- /api/courses/* → Course Service
- /api/students/* → Student Service

---

# Inter-Service Communication

The Student Service communicates with the Course Service using HTTP requests through Python's `requests` library.

Flow:

Postman
↓
API Gateway
↓
Student Service
↓
Course Service
↓
Student Service
↓
API Gateway
↓
Postman

---

# Error Handling

If the Course Service is unavailable, the Student Service returns:

HTTP Status Code: **503 Service Unavailable**

Example Response:

```json
{
    "message": "Course Service Unavailable"
}
```

---

# Synchronous Communication

Synchronous communication uses direct HTTP requests.

Advantages:

- Simple to implement
- Immediate response
- Easy to understand

Disadvantages:

- Services are tightly coupled
- If one service is down, the request fails

---

# Asynchronous Communication

Asynchronous communication uses a message broker such as RabbitMQ or Kafka.

Advantages:

- Loose coupling
- Better scalability
- Services work independently

Disadvantages:

- More complex to implement
- Eventual consistency

---

# When to Use RabbitMQ or Kafka

Use message queues for:

- Email notifications
- SMS notifications
- Background jobs
- Event processing
- Logging
- Large-scale distributed systems

---

# Technologies Used

- Python
- Flask
- Requests Library
- SQLite
- VS Code
- Postman

---

# Conclusion
Successfully implemented a simple Microservices Architecture by separating the Course Management application into independent services, enabling inter-service communication, handling service failures, and routing requests through an API Gateway.