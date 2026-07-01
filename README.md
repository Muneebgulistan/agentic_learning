# Agentic Learning

A clean and beginner-friendly FastAPI project designed for learning API development, routing, and query/path parameters in Python.

## ✨ Overview

This project showcases a simple REST API built with FastAPI. It includes:

- A home endpoint for testing the server
- A path parameter example for student lookup
- A query parameter example for search functionality

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn

## 🚀 Getting Started

1. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install the dependencies
   ```bash
   pip install fastapi uvicorn
   ```

3. Run the application
   ```bash
   uvicorn my_first_api.main:app --reload
   ```

4. Open your browser and visit:
   - http://127.0.0.1:8000/
   - http://127.0.0.1:8000/docs

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Returns a welcome message |
| GET | /student/{student_id} | Returns a student record based on the provided ID |
| GET | /search | Searches for a student using a query parameter |

## 📁 Project Structure

```text
agentic_learning/
├── my_first_api/
│   └── main.py
└── README.md
```

## 🎯 Purpose

This repository is intended for learning and practicing the basics of building APIs with FastAPI in a simple, structured way.
