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
