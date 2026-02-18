# CLAUDE.md - Art Moving Business (EJ Art Mover)

## Project Overview
Django web application for managing art transportation services — work orders, scheduling, invoicing, and client management. Deployed on Heroku with Docker.

## Quick Commands

```bash
# Local development
source .venv/bin/activate
python manage.py runserver

# Docker
docker compose up --build

# Database
python manage.py migrate
python manage.py createsuperuser

# Checks & Tests
python manage.py check
python manage.py test

# Static files
python manage.py collectstatic --noinput

# Deploy to Heroku
git push heroku main
```

## Project Structure

| Directory | Purpose |
|-----------|---------|
| `django_project/` | Settings, URLs, WSGI config |
| `accounts/` | Custom user auth (`CustomUser` extending AbstractUser) |
| `pages/` | Landing page / dashboard |
| `workorders/` | Core: work orders, events, attachments, notes, PDF generation |
| `clients/` | Client CRUD |
| `invoices/` | Invoice tracking (unpaid → in_quickbooks → paid), PDF generation |
| `calendar_app/` | FullCalendar week/day views, drag-and-drop ordering |
| `templates/` | HTML templates (Bootstrap 5) |
| `static/` | CSS, JS, images |

## Key Files

- `workorders/queries.py` — Centralized optimized queries (`WorkOrderQueries` class)
- `workorders/storage.py` — Custom Cloudinary storage (images vs raw documents)
- `workorders/views.py` — Main views, imports `WorkOrderQueries` from queries.py
- `django_project/settings.py` — All config, env-based via `django-environ`

## Tech Stack

- **Backend:** Django 5.1.6, Gunicorn (2 workers, 120s timeout)
- **Database:** PostgreSQL (via `DATABASE_URL`)
- **Storage:** Cloudinary (media), WhiteNoise (static)
- **PDF:** WeasyPrint
- **Frontend:** Bootstrap 5, FullCalendar, Flatpickr, Select2 (all CDN)
- **Deploy:** Heroku (Docker container, Basic dyno)

## Environment Variables

Required in `.env`:
- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DATABASE_URL`
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

## Domain

- Production: `ejartmover.net` / `art-moving-buisness-0a734245a61f.herokuapp.com`

## Important Patterns

- All views use `@login_required` — the app is fully authenticated
- State-changing actions use `@require_POST` (mark_completed, mark_paid, etc.)
- Templates already use `<form method="post">` with `{% csrf_token %}` for all POST actions
- `WorkOrderQueries` in `workorders/queries.py` is the single source for optimized querysets — do not duplicate
- Invoice statuses flow: `unpaid` → `in_quickbooks` → `paid`
- Work order statuses: `pending` → `in_progress` → `completed`
- File uploads: max 10MB, images get thumbnails, documents stored as Cloudinary "raw"
