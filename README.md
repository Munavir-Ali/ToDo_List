# 📝 Django ToDo App

> **Internship Project at Futuro IT Solutions**

A full-stack ToDo list application developed using Django as part of my internship. The project uses Django's admin panel for task management, following clean and modular architecture.

---

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap optional)
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

todoproject/
├── manage.py
├── todo/ # Main app
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ └── ...
├── todoproject/ # Project folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── templates/ # HTML templates (if any)
├── db.sqlite3 # Development database
└── screenshots/ # UI screenshots for documentation

yaml
Copy code

---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Munavir-Ali/ToDo_App.git
cd ToDo_App

# Create virtual environment
python -m venv env
env\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
## 📸 Screenshots

### 🏠 Home Page

![Home Page](https://github.com/Munavir-Ali/ToDo_App/blob/main/screenshots/home_page.png)

---

### ⚙️ Django Admin Panel

![Admin Page](https://github.com/Munavir-Ali/ToDo_App/blob/main/screenshots/django_admin_page.png)

⚙️ Django Admin Panel

🧠 About the Developer
This project was developed as part of my internship at Futuro IT Solutions during my B.Tech in Computer Science. It showcases backend development using Django and effective use of Django’s built-in admin interface.

📄 License
This project is open source and available under the MIT License.

yaml
Copy code

---

✅ You can now:
1. Save this as your `README.md` file.
2. Run the following to push:

```bash
git add README.md
git commit -m "Updated full README with project info and screenshots"
git push origin main
