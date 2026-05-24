# V2 Labs - Django REST API Backend

This is the backend API engine for **V2 Labs**, handling client project leads, contact submissions, and admin data. It is powered by **Django 4.2** and **Django REST Framework (DRF)**.

## Core Setup Details

- **App Name**: `api`
- **Models**:
  - `ProjectLead`: Stores client inquiries, names, emails, phones, selected service types, estimated budgets, and project descriptions.
- **REST Endpoints**:
  - `POST /api/contact/`: Receives project request lead from frontend form. Saves to database and returns a thank you response.
  - `GET /api/contact/`: Health check returns active API message and service options.
- **Security Features**:
  - CORS Headers configured to resolve origin permissions in container networks.

---

## 🛠️ Getting Started Locally

### 1. Initialize Virtual Environment & Install Requirements

1. Navigate to this directory (`v2-backend`).
2. Activate the pre-created virtual environment:
   - **Windows PowerShell**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows Command Prompt (CMD)**:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
3. Install requirements (optional if already completed):
   ```bash
   pip install -r requirements.txt
   ```

### 2. Database Migrations

Apply standard SQLite migrations to create `db.sqlite3` file and tables:
```bash
python manage.py migrate
```

### 3. Start Development Server

```bash
python manage.py runserver
```
- Access the API homepage at: [http://localhost:8000/api/contact/](http://localhost:8000/api/contact/)

---

## 🐋 Docker Container Commands

- **Build Docker Image**:
  ```bash
  docker build -t v2labs-backend .
  ```
- **Run Container**:
  ```bash
  docker run -p 8000:8000 v2labs-backend
  ```
