# 🖼️ Art Moving Business Management System

A full-featured Django web application designed to streamline the operations of an art transportation business. Built for real-world logistics, it supports client management, work order scheduling, invoice tracking, and interactive calendar views — all with a modern, mobile-responsive interface.

---

## 🚀 Features

- 🔐 **User Authentication** – Custom user model with signup, login, logout
- 📋 **Client Management** – Full CRUD with search and detail views
- 📦 **Work Orders** – Dynamic event scheduling (pickup, install, etc.), notes, attachments
- 📅 **Interactive Calendar** – FullCalendar integration with clickable events
- 💸 **Invoicing System** – Track paid, unpaid, and overdue invoices with due date controls
- 🖨️ **Printable Invoices** – PDF-ready invoice views for clients and records
- 📎 **File Uploads** – Attach documents and photos to work orders
- 🌐 **Mobile-Friendly UI** – Responsive design using Bootstrap 5 and custom SCSS
- 🐳 **Dockerized** – Production-ready Docker environment with PostgreSQL and Gunicorn
- ☁️ **Deployed on Heroku** – Container-based deployment using `heroku.yml`

---

## 🛠️ Tech Stack

| Layer      | Tech                                 |
|------------|--------------------------------------|
| Backend    | Django 5.1.6, Django REST Framework   |
| Frontend   | Bootstrap 5, FullCalendar, Flatpickr |
| Auth       | Custom `User` model with Crispy Forms|
| DB         | PostgreSQL (Dockerized)              |
| Deploy     | Docker, Heroku, Gunicorn, Whitenoise |
| Styling    | SCSS, Bootstrap Icons                |

---

## ⚙️ Setup (Development)

```bash
# Clone the repo
git clone https://github.com/yourusername/art-moving-business.git
cd art-moving-business

# Build and run the app
docker compose up --build

# Access the app
http://localhost:8080
# art_moving_buisness
