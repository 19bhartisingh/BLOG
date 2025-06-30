# 📝 FastAPI Blog Web App

A simple blogging REST API built using **FastAPI**. This project supports essential CRUD operations for blog posts (Create, Read, Update, Delete) and provides secure **user authentication** using **JWT tokens**.

---

## 🚀 Features

* ✅ Create, Read, Update, and Delete blog posts
* 👤 User registration and secure login
* 🔐 JWT-based authentication for protected routes
* 📦 Built with FastAPI and SQLAlchemy
* 🧪 Interactive API docs with Swagger (`/docs`)

---

## 📂 Project Structure

blog/

├── __init__.py

├── database.py             # DB connection setup

├── hashing.py              # Password hashing logic

├── main.py                 # Application entry point

├── oauth2.py               # OAuth2 and JWT token validation

├── schemas.py              # Pydantic schemas for request/response models

├── token.py                # Token generation and management

├── routers/                # Contains API route logic

│       ├── __init__.py

│       ├── authentication.py     # Login route and token issuing

│       ├── blog.py               # Blog CRUD routes

│       └── user.py               # User-related routes

├── repository/               # Contains actual database logic separated from routes

│          ├── blog.py               # Blog DB operations

│          └── user.py               # User DB operations


---

## 📌 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/fastapi-blog.git
   cd fastapi-blog
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to:

   * Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   * Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠 Tech Stack

* **FastAPI** – high-performance API framework
* **Pydantic** – for data validation
* **SQLAlchemy** – ORM for database operations
* **JWT** – for authentication
* **Uvicorn** – ASGI server

---

## 🔐 Authentication Flow

* Register a new user via `/user` route.
* Login via `/UserLogin` and get a JWT token.
* Use the token in the **Authorize** section of Swagger UI to access protected endpoints (`/blog`).

---

## 🙌 Credits

This project is inspired by and built while learning from the amazing [**Bitfumes FastAPI Tutorial Series** on YouTube](https://www.youtube.com/bitfumes). 


