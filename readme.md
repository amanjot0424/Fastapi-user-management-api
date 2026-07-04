# 🚀 FastAPI User Management API

A RESTful User Management API built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **JWT Authentication**. This project demonstrates secure user authentication, password hashing, CRUD operations, and modular API development.

---

## ✨ Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing using BCrypt
- Protected Routes
- CRUD Operations
- SQLAlchemy ORM
- Environment Variables using `.env`
- Modular Project Structure with APIRouter

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn
- Python-dotenv

---

## 📁 Project Structure

```text
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── security.py
├── routers/
│   ├── auth.py
│   └── users.py
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/amanjot0424/Fastapi-user-management-api.git
```

Move into the project:

```bash
cd Fastapi-user-management-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///new.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📖 API Endpoints

### Authentication

- POST `/auth/login`
- GET `/auth/profile`

### Users

- POST `/users`
- GET `/users`
- GET `/users/{id}`
- PUT `/users/{id}`
- DELETE `/users/{id}`

---

## 📄 API Documentation

After running the project:

```
http://127.0.0.1:8000/docs
```

---

## 👨‍💻 Author

**Amanjot Singh**

B.Tech CSE Student | Aspiring AI Engineer | Python & Data Analytics Enthusiast