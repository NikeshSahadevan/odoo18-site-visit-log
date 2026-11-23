# Site Visit Log — Custom Odoo 18 Module

A full-featured custom Odoo 18 ERP application built to log, schedule, track, and report customer field visits.

## Key Features
- **Auto-Sequence Reference (ir.sequence)**: Automatically generates unique visit IDs (SV/2026/0001).
- **CRM & Contacts Integration (_inherit)**: Extends es.partner with a Smart Button showing visit counts per customer and auto-populated phone details.
- **Multi-View Interface**:
  - **List View**: Colored status badges and salesperson avatars.
  - **Kanban View**: Drag-and-drop workflow cards grouped by stage (Draft / Done).
  - **Calendar View**: Color-coded monthly/weekly schedule view by salesperson.
  - **Form & Search Views**: Statusbar workflow buttons, custom filters (My Visits, Draft, Done), and multi-level Group By.
- **Business Logic & Validation**: Computed visit summary (@api.depends) and future-date validation constraints (@api.constrains).
- **Audit Chatter (mail.thread)**: Full field tracking and activity scheduling.
- **QWeb PDF Reporting**: Printable Site Visit Report with company header/footer layout (wkhtmltopdf).
- **Security & Multi-User Access**: Configured ACL (ir.model.access.csv) and row-level Record Rules (ir.rule) separating personal visits from admin/manager views.

## Tech Stack
- **Framework**: Odoo 18 Community Edition
- **Backend**: Python 3.11+ (Odoo ORM)
- **Frontend / Views**: XML, QWeb
- **Database**: PostgreSQL
