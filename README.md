# fastapi-ecommerce-project
A FastAPI-based E-Commerce Product Management API with MySQL, SQLAlchemy, CRUD operations, Postman testing, and 25 product records across 5 categories.

# - FastAPI E-Commerce Product Management API

##  Project Overview

The **FastAPI E-Commerce Product Management API** is a RESTful backend application developed using **FastAPI**, **SQLAlchemy (Object Relational Mapper - ORM)**, **Pydantic**, and **MySQL**. This project demonstrates complete **CRUD (Create, Read, Update, Delete)** operations for managing products in an e-commerce system.

The application enables users to create, retrieve, update, and delete product information while securely storing data in a MySQL database. It also provides category-based product retrieval and interactive API documentation using FastAPI's built-in **Swagger UI** and **ReDoc**.

This project was developed as a hands-on learning project to strengthen backend development skills, database integration, REST API development, API testing, database management, and version control using **Git** and **GitHub**.

---

# -> Features

-  Create New Products
-  Retrieve All Products
-  Retrieve Product by ID
-  Update Existing Products
-  Delete Products
-  Retrieve Products by Category
-  RESTful API Design
-  MySQL Database Integration
-  SQLAlchemy (Object Relational Mapper - ORM)
-  Pydantic Data Validation
-  Interactive API Documentation
-  API Testing using Postman

---

#  Product Categories

The project contains **25 sample product records** distributed across **5 different product categories**.

| Category | Records |
|----------|---------|
| 👕 Clothes | 5 |
| 🥤 Beverages | 5 |
| 📱 Electronic Devices | 5 |
| 🎒 Accessories | 5 |
| 💄 Beauty & Personal Care | 5 |

---

#  Technologies Used

- 🐍 Python 3
- ⚡ FastAPI
- 🔗 SQLAlchemy (ORM)
- 📋 Pydantic
- 🗄️ MySQL
- 🚀 Uvicorn
- 📮 Postman
- 📖 Swagger UI
- 📚 ReDoc
- 🛠️ MySQL Workbench
- 🌿 Git
- 💻 GitHub

---

# 📂 Project Structure

```text
fastapi-ecommerce-project/
│
├── main.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── seed_data.py
├── requirements.txt
└── README.md
```

---

#  API Endpoints

| HTTP Method | Endpoint | Description |
|-------------|----------|-------------|
| GET | `/` | Welcome Message |
| POST | `/products` | Create Product |
| GET | `/products` | Retrieve All Products |
| GET | `/products/{product_id}` | Retrieve Product by ID |
| PUT | `/products/{product_id}` | Update Product |
| DELETE | `/products/{product_id}` | Delete Product |
| GET | `/category/{category_name}` | Retrieve Products by Category |

---

# 💾 Database

- **Database:** MySQL
- **ORM:** SQLAlchemy (Object Relational Mapper)
- **Validation:** Pydantic

All product information is stored and managed in a MySQL database using SQLAlchemy ORM.

---

# 🧪 API Testing

The API was successfully tested using:

- ✅ FastAPI Swagger UI (`/docs`)
- ✅ FastAPI ReDoc (`/redoc`)
- ✅ Postman
- ✅ MySQL Workbench

All CRUD operations (Create, Read, Update, Delete) were successfully verified.

---

# ▶️ Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/Saisree-11/fastapi-ecommerce-project.git
```

## Navigate to the Project

```bash
cd fastapi-ecommerce-project
```

## Create a Virtual Environment

```bash
python -m venv env
```

## Activate the Virtual Environment (Windows)

```bash
env\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure the Database

Create a MySQL database named `ecommerce_db`, then set your connection string via an environment variable (recommended) or update the default in `database.py`:

```bash
set DATABASE_URL=mysql+pymysql://<username>:<password>@localhost:3306/ecommerce_db
```

## Seed Sample Data (Optional)

```bash
python seed_data.py
```

## Run the Application

```bash
uvicorn main:app --reload
```

---

# 📖 API Documentation

After running the application, access the following URLs:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- FastAPI Framework
- REST API Development
- CRUD (Create, Read, Update, Delete) Operations
- SQLAlchemy (Object Relational Mapper - ORM)
- MySQL Database Integration
- Pydantic Request & Response Models
- API Validation
- API Testing using Postman
- Interactive API Documentation
- Git Version Control
- GitHub Repository Management
- Backend Project Structure & Best Practices

---

# 🔮 Future Enhancements

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 🔍 Product Search Functionality
- 📄 Pagination
- 🖼️ Product Image Upload
- 🛒 Order Management
- 👥 Customer Management
- 🔒 Role-Based Authorization
- 🐳 Docker Deployment
- ☁️ Cloud Deployment

---

# 👨‍💻 Author

## Sai Sree

**AI & Data Science Student | Python Developer | FastAPI Learner**

### 🔗 Connect with Me

**GitHub**
https://github.com/Saisree-11

**LinkedIn**
https://www.linkedin.com/in/saisree11
