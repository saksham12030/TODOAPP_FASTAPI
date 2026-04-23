# 📝 Todo API (FastAPI + SQLAlchemy)

A simple yet structured backend API for managing todos, built using **FastAPI** and **SQLAlchemy** with a clean architecture approach.

---

## 🚀 Features

* Create, Read, Delete Todos
* RESTful API design
* Database integration using SQLAlchemy ORM
* Environment variable support using dotenv
* Clean dependency injection using FastAPI
* Response validation using Pydantic

---

## 🧠 Tech Stack

* **Backend**: FastAPI
* **Database ORM**: SQLAlchemy
* **Database**: MySQL (configurable)
* **Environment Management**: python-dotenv
* **Validation**: Pydantic

---

## 📂 Project Structure

```
.
├── main.py          # FastAPI app and routes
├── models.py        # SQLAlchemy models
├── database.py      # DB connection setup
├── .env             # Environment variables
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/todo-api-fastapi.git
cd TODOAPP_FASTAPI
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file:

```
DATABASE_URL=your_database_url
```

Example:

```
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/tododb
```

---

## ▶️ Run the Server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

### 🔹 Get All Todos

```
GET /todos
```

### 🔹 Get Single Todo

```
GET /todos/{id}
```

### 🔹 Create Todo

```
POST /todos
```

Body:

```
{
  "title": "Learn FastAPI",
  "description": "Build backend project",
  "completed": false
}
```

### 🔹 Delete Todo

```
DELETE /todos/{id}
```

---

## 📊 API Docs (Auto-generated)

FastAPI provides interactive API docs:

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

