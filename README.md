# FastAPI JWT Authentication with Role-Based Access (RBAC)

A secure RESTful API built with **FastAPI**, **SQLModel**, and **PostgreSQL**, implementing **JWT-based authentication** and **role-based access control (RBAC)**. This project manages users and projects, with access control depending on whether a user is an `admin` or a regular `user`.


## Features

- User Registration (with role)
- Password Hashing using `bcrypt`
- JWT Token-based Login
- Role-Based Access Control (`admin`, `user`)
- CRUD for Projects
- Assign Projects to Users (admin only)
- Protected routes with token validation
- Get Current Logged-In User (`/auth/me`)

---

## Tech Stack

- **FastAPI** – Web framework
- **SQLModel** – ORM
- **PostgreSQL** – Relational database
- **bcrypt** – Secure password hashing
- **python-jose** – JWT encoding/decoding
- **Uvicorn** – ASGI server

---

## Installation Steps

1. **Clone the repository**
   - git clone https://github.com/<your-username>/fastapi-jwt-rbac.git
   - cd fastapi-jwt-rbac

2. **Create and activate virtual environment**
    - python -m venv venv
    - venv\Scripts\activate  # On Windows

3. **Install Dependencies**
    - pip install -r requirements.txt

4. **Set up environment variables**

    Create a .env file in the root directory and add:
    - DATABASE_URL=postgresql://postgres:<your_password>@localhost:5432/<your_database>
    - SECRET_KEY=your_secret_key
    - ALGORITHM=HS256
    - ACCESS_TOKEN_EXPIRE_MINUTES=30

5. **Run the Server**
    - uvicorn app.main:app --reload


## 📬 Postman Collection

You can test all APIs using the official Postman collection:

👉 [Download Collection](postman-collection/fastapi.postman_collection.json)

1. Open Postman
2. Click **Import**
3. Choose the downloaded `.json` file
4. Run requests directly with saved headers, bodies, and tokens