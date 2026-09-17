# Student Attendance Management System

A full-stack CRUD web application for managing student records and daily
attendance, built with **React**, **Django REST Framework**, and
**SQLite**.

---

## 1. Project Overview
This project digitizes student and attendance record-keeping for a
college department. Staff can add, view, update, and delete student
records, mark daily attendance as Present/Absent, and view live
attendance statistics on a dashboard — all backed by a real database, not
mock data.

## 2. Problem Statement
Manual attendance registers and spreadsheets are slow to search, easy to
lose, and hard to analyze. This system replaces that process with a
simple web application backed by a proper relational database and REST
API.

## 3. Objectives
- Implement complete CRUD operations for Students and Attendance.
- Enforce validation on both frontend and backend.
- Prevent duplicate roll numbers and duplicate attendance entries.
- Provide live, database-driven dashboard statistics.
- Support search and filtering for both students and attendance records.
- Use only self-hosted technology — no Firebase, Supabase, or other BaaS.

## 4. Features
- Add / View / Edit / Delete students
- Mark attendance as Present or Absent
- Edit or delete attendance records
- Search students by name or roll number
- Filter students by department, year, section
- Filter attendance by date and status
- Dashboard with total students, present count, absent count, and
  attendance percentage
- Client-side and server-side validation with friendly error messages
- Delete confirmation dialogs
- Loading and empty-state messages throughout the UI

## 5. Technology Stack

| Layer            | Technology                              |
|-------------------|------------------------------------------|
| Frontend           | React, Vite, JavaScript, HTML, CSS, Axios |
| Backend            | Python, Django, Django REST Framework     |
| Database           | SQLite                                    |
| API Testing        | Postman                                   |
| Version Control    | Git, GitHub                               |

## 6. System Architecture

```
React frontend (port 5173)
        |  Axios (HTTP/JSON)
        v
Django REST Framework API (port 8000)
        |  Django ORM
        v
SQLite database
```

See [`docs/architecture.md`](docs/architecture.md) for full details.

## 7. Project Structure

```
student-attendance-management/
├── README.md
├── .gitignore
├── LICENSE
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── config/            # Django project settings & URLs
│   ├── attendance/        # Django app: models, serializers, views, tests
│   └── database/          # SQLite file is generated here
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── .env.example
│   └── src/
│       ├── components/    # React components
│       └── services/      # Axios API client
├── docs/                  # Full project documentation
├── postman/               # Postman collection for API testing
└── screenshots/           # Application screenshots
```

## 8. Database Description
Two tables: `Student` and `Attendance`, linked by a foreign key
(`Student 1 ──< Many Attendance`). Full schema, constraints, and an ER
diagram are documented in [`docs/database-design.md`](docs/database-design.md).

## 9. API Endpoints

| Method | Endpoint                 | Purpose                    |
|--------|---------------------------|------------------------------|
| POST   | `/api/students/`           | Create a student             |
| GET    | `/api/students/`           | List all students            |
| GET    | `/api/students/{id}/`      | Retrieve one student          |
| PATCH  | `/api/students/{id}/`      | Update a student              |
| DELETE | `/api/students/{id}/`      | Delete a student               |
| POST   | `/api/attendance/`         | Create an attendance record    |
| GET    | `/api/attendance/`         | List all attendance records    |
| GET    | `/api/attendance/{id}/`    | Retrieve one attendance record |
| PATCH  | `/api/attendance/{id}/`    | Update an attendance record    |
| DELETE | `/api/attendance/{id}/`    | Delete an attendance record    |
| GET    | `/api/dashboard/`          | Get live dashboard statistics  |

Full request/response examples: [`docs/api-documentation.md`](docs/api-documentation.md).

## 10. CRUD Operations
All CRUD flows (Create, Read, Update, Delete) for both Student and
Attendance are explained step by step in
[`docs/crud-implementation.md`](docs/crud-implementation.md).

## 11. Validation
Implemented on **both** ends:
- **Frontend:** required fields, valid email format, year range, valid
  status, shown as inline field errors.
- **Backend (authoritative):** DRF serializer validation for required
  fields, unique roll number/email, year range, valid status choice, valid
  foreign key, and duplicate attendance prevention. The frontend never
  relies solely on client-side checks.

## 12. Testing
Automated tests live in `backend/attendance/tests.py` and cover student
and attendance CRUD, validation errors, duplicate checks, and the
dashboard endpoint. Run with:

```bash
cd backend
python manage.py test
```

See the full test case table in [`docs/testing.md`](docs/testing.md).

## 13. Installation Steps
Full instructions: [`docs/installation.md`](docs/installation.md).

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```
Backend runs at `http://127.0.0.1:8000/`

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
Frontend runs at `http://localhost:5173/`

### How to Run the Application
1. Start the backend (`python manage.py runserver`) in one terminal.
2. Start the frontend (`npm run dev`) in another terminal.
3. Open `http://localhost:5173/` in your browser.

## 14. Postman Testing
Import [`postman/student-attendance-api.json`](postman/student-attendance-api.json)
into Postman to manually test every CRUD endpoint against
`http://127.0.0.1:8000`.

## 15. Screenshots
See [`screenshots/README.md`](screenshots/README.md) for the list of
screenshots to capture and add before final submission.

## 16. Challenges and Solutions
See [`docs/challenges-and-solutions.md`](docs/challenges-and-solutions.md)
for a breakdown of key implementation challenges (duplicate prevention,
CORS, consistent error handling, dual validation) and how each was solved.

## 17. Future Enhancements
See [`docs/future-enhancements.md`](docs/future-enhancements.md) for ideas
such as authentication, bulk attendance marking, reports/export, and
analytics charts.

## 18. GitHub Usage
This project is version-controlled with Git and hosted on GitHub. Typical
workflow:

```bash
git init
git add .
git commit -m "Initial commit: Student Attendance Management System"
git branch -M main
git remote add origin https://github.com/<your-username>/student-attendance-management.git
git push -u origin main
```

Sensitive files (`.env`, `venv/`, `node_modules/`, `db.sqlite3`) are
excluded via `.gitignore` and never committed. Use the provided
`.env.example` files as templates.

## 19. Security Notes
- No secrets, API keys, or credentials are committed to the repository.
- `backend/.env.example` and `frontend/.env.example` show what
  environment variables are needed without exposing real values.
- The Django `SECRET_KEY` is read from an environment variable
  (`DJANGO_SECRET_KEY`) with a clearly-marked development-only fallback —
  replace it before any real deployment.

## 20. License
This project is licensed under the [MIT License](LICENSE).

---

### Quick Reference: Default Ports
| Service   | URL                          |
|-----------|-------------------------------|
| Backend   | http://127.0.0.1:8000          |
| Frontend  | http://localhost:5173          |
| API base  | http://127.0.0.1:8000/api      |
