# ✂️ Tailor Shop Measurement Management System

A full-stack Customer & Garment Measurement Management application designed for bespoke tailoring shops. This project provides a fast, reliable RESTful API built with **FastAPI** and **SQLAlchemy ORM** backed by a **MySQL** database, paired with an interactive frontend dashboard for managing client profiles and custom clothing measurements.

---

## ✨ Features

* **Complete Customer CRUD Operations:** Create, read, update, and delete customer profiles and measurement records seamlessly.
* **Detailed Garment Specifications:** Track specific measurements for shirts (`shirt_shoulder`, `shirt_length`, `shirt_hand`) and trousers (`pants_length`, `pants_style`, `pants_waist`).
* **Data Validation & Serialization:** Powered by **Pydantic** schemas (`UserCreate`, `UserResponse`) to ensure strict type checking and clean API responses.
* **Database ORM Integration:** Uses **SQLAlchemy** with `PyMySQL` for automatic table generation and relational mapping.
* **CORS Enabled:** Configured with FastAPI `CORSMiddleware` for smooth integration with local and external frontend clients.
* **Interactive API Documentation:** Automatic Swagger UI (`/docs`) and ReDoc (`/redoc`) generation out of the box.

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python)
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Database Driver:** PyMySQL
* **ASGI Server:** Uvicorn
* **Frontend:** HTML5, CSS3, Vanilla JavaScript

---

## 📂 Project Structure

```text
├── database.py      # MySQL database connection, SQLAlchemy engine, and session dependency
├── models.py        # SQLAlchemy ORM table schema ('cloths')
├── schemas.py       # Pydantic models for request validation and response serialization
├── main.py          # FastAPI application, CORS setup, and CRUD route handlers
├── index.html       # Frontend dashboard for managing customer measurements
└── README.md        # Project documentation

Getting Started
1. Prerequisites
Python 3.9+ installed

MySQL Server running locally on port 3306

2. Clone the Repository
Bash
git clone [https://github.com/your-username/tailor-measurement-system.git](https://github.com/your-username/tailor-measurement-system.git)
cd tailor-measurement-system
3. Install Dependencies
Bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
4. Configure MySQL Database
Open your MySQL client and create the database:

SQL
CREATE DATABASE project;
Update the connection string in database.py with your MySQL credentials:

Python
DATABASE_URL = "mysql+pymysql://<username>:<password>@localhost:3306/project"
5. Run the FastAPI Server
Bash
uvicorn main:app --reload
API Base URL: http://127.0.0.1:8000

Swagger UI Docs: http://127.0.0.1:8000/docs

6. Launch the Frontend
Simply open index.html in any web browser (or serve it via VS Code Live Server) to interact with the backend API visually.

📜 License
This project is open-source and available under the MIT License.
