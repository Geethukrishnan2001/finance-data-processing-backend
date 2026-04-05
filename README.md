# Finance Data Processing Backend

A backend system built using **Django** and **Django REST Framework (DRF)** to manage financial records with role-based access control and dashboard analytics.

# Features

* User and Role Management (Admin, Analyst, Viewer)
* Financial Records CRUD (Create, Read, Update, Delete)
* Record Filtering (by type, category, date)
* Dashboard Summary API (total income, expenses, net balance)
* Role-Based Access Control (RBAC)
* Input Validation and Error Handling
* Data Persistence using SQLite

# Tech Stack

* Python 3.x
* Django
* Django REST Framework (DRF)
* SQLite

# Project Structure

finance-data-processing-backend/
│
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│
├── finance_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── db.sqlite3
├── README.md

# Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/finance-data-processing-backend.git
cd finance-data-processing-backend

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install django djangorestframework

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Create Superuser (for admin panel)

python manage.py createsuperuser

6. Run the Server

python manage.py runserver

# API Endpoints

Users

* `GET /users/` → List users
* `POST /users/` → Create user
* `GET /users/{id}/` → Retrieve user
* `PUT /users/{id}/` → Update user
* `DELETE /users/{id}/` → Delete user

Financial Records

* `GET /records/` → List records
* `POST /records/` → Create record
* `GET /records/{id}/` → Retrieve record
* `PUT /records/{id}/` → Update record
* `DELETE /records/{id}/` → Delete record

Filtering Examples

/records/?type=income
/records/?category=food
/records/?date=2026-04-05

Dashboard API

* `GET /dashboard/`

Example Response:

json
{
  "total_income": 5000,
  "total_expense": 2000,
  "net_balance": 3000
}


# Role-Based Access Control

| Role    | Permissions                          |
| ------- | ------------------------------------ |
| Admin   | Full access (create, update, delete) |
| Analyst | Read-only access                     |
| Viewer  | Read-only access                     |


# Validation Rules

* Amount must be greater than 0
* Type must be either `income` or `expense`
* Required fields must be provided
* Invalid inputs return proper error responses

# Limitations

* Basic authentication (no JWT)
* No pagination implemented
* No frontend (API-only project)

# Future Improvements

* JWT Authentication
* Pagination & Search
* Unit and Integration Testing
* Deployment (AWS / Render / Railway)
* Advanced filtering and analytics

# Testing

You can test APIs using:

* Postman
* Browser (for GET requests)
* Django Admin Panel

# Admin Panel

Access Django admin at:

http://127.0.0.1:8000/admin/

Use superuser credentials to:

* Manage users
* Add/edit financial records

# Author

**Geethu Krishnan**

# Notes

This project was developed as part of a backend assignment to demonstrate:

* API design
* Data modeling
* Role-based access control
* Validation and error handling

If you found this project useful, feel free to star the repository!
