# 📝 Django ToDo App

> **Internship Project at Futuro IT Solutions**

A full-stack ToDo list application developed using Django as part of my internship. The project uses Django's admin panel for task management, following clean and modular architecture.

---

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (optional Bootstrap)
- **Database**: SQLite
- **Admin Interface**: Django Admin Panel

---

## ✨ Features

- Task model with fields:
  - Title
  - Description
  - Completion status
- CRUD operations via Django Admin
- Admin-based interface for managing ToDo items
- Modular folder structure using Django best practices

---

## 📁 Project Structure

todo-app/
├── manage.py
├── todo/ # Main app
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ └── ...
├── todo_project/ # Project folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── templates/ # HTML templates (if any)

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/todo-app.git
cd todo-app

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the server
python manage.py runserver
