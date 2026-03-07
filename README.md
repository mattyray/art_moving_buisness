# EJ Art Mover — Business Management System

A production Django application built for a real art transportation business. It handles the full operational workflow — client management, work order scheduling, drag-and-drop calendar planning, invoicing, PDF generation, and file attachments — all behind a fully authenticated, mobile-responsive interface.

**Live at:** [ejartmover.net](https://ejartmover.net)

---

## What It Does

This app replaces spreadsheets and paper for a small art logistics company. The core workflow:

1. **Create a client** with contact info and addresses
2. **Open a work order** describing the job (e.g., "Move 3 paintings from gallery to collector's home")
3. **Schedule events** on the work order — pickups, wraps, installs, deliveries — each with their own date and address
4. **Plan the day** using an interactive calendar with drag-and-drop reordering and time assignments
5. **Track progress** with status updates, notes, and photo/document attachments
6. **Generate an invoice** from the work order, track payment status, and print a PDF

---

## Key Features

### Work Orders
- Multi-event scheduling per job (pickup, wrap, install, deliver, drop off)
- Status tracking: `pending` → `in_progress` → `completed`
- Notes and file attachments (images get thumbnails, documents stored as raw files)
- 10MB upload limit with Cloudinary storage

### Calendar
- Weekly and daily views powered by FullCalendar
- Day view with drag-and-drop event reordering (SortableJS)
- Time assignment per event with inline editing
- Saves order and times via AJAX

### Invoicing
- Auto-generated from work orders or created standalone
- Status flow: `unpaid` → `in_quickbooks` → `paid`
- PDF generation with WeasyPrint — styled for print with company branding

### PDF Generation
- Work order PDFs: client info, job details, all events, notes, attachments list
- Invoice PDFs: bill-to info, services provided, amount due, payment instructions
- A4 format, print-optimized CSS with page break handling

### Client Management
- Full CRUD with search
- Linked work orders and invoices visible from client detail

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 5.1.6, Python 3.10 |
| **Database** | PostgreSQL (via `DATABASE_URL`) |
| **PDF** | WeasyPrint |
| **File Storage** | Cloudinary (media), WhiteNoise (static) |
| **Frontend** | Bootstrap 5, FullCalendar, SortableJS, Flatpickr, Select2 |
| **Auth** | Custom user model extending `AbstractUser`, all views `@login_required` |
| **Deploy** | Docker container on Heroku (Basic dyno), Gunicorn |
| **Domain** | ejartmover.net |

---

## Architecture Highlights

- **Centralized query layer** — `WorkOrderQueries` class handles all optimized querysets with `select_related` / `prefetch_related` to avoid N+1 problems
- **Custom Cloudinary storage** — separate handling for images (with thumbnails) vs. raw document uploads
- **Security hardened** — CSRF protection on all forms and AJAX, `SECURE_HSTS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_HTTPONLY`, `Content-Type-Nosniff`, `X-Frame-Options: DENY`
- **Mobile-first** — responsive layouts, iOS keyboard viewport handling (`interactive-widget=resizes-content`, `dvh` units)
- **State-changing actions use `@require_POST`** — prevents accidental GET-triggered mutations

---

## Project Structure

```
django_project/     # Settings, URLs, WSGI
accounts/           # Custom user authentication
pages/              # Landing page / dashboard
workorders/         # Core: work orders, events, attachments, notes, PDF
clients/            # Client CRUD
invoices/           # Invoice tracking and PDF generation
calendar_app/       # FullCalendar views, drag-and-drop day planning
templates/          # Django templates (Bootstrap 5)
static/             # CSS, JS, images
```

---

## Note

This is a production application built for a real business — not a template or starter project. The repo is public as a portfolio piece to demonstrate full-stack Django development, from data modeling through deployment.
