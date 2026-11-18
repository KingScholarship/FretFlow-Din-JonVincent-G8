# FretFlow

FretFlow is a Django workspace for managing guitar songs, charts, and live setlists. It uses Supabase PostgreSQL for application data.

## Project flow

| App | Status | Scope |
| --- | --- | --- |
| Accounts | Complete | Registration, login/logout, member/admin dashboards, and profile editing |
| Songs | Pending | Personal song catalog, chart formatting, transposition, chord diagrams, and auto-scroll |
| Setlists | Pending | Setlist management and stage view |

Build the apps in order: Accounts, Songs, then Setlists.

## Local setup

1. Install dependencies:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` if `.env` does not already exist. Fill in the Django secret and Supabase PostgreSQL connection values. Keep `.env` private; it is ignored by Git.

3. Apply migrations and create an administrator:

   ```powershell
   .\.venv\Scripts\python.exe manage.py migrate
   .\.venv\Scripts\python.exe manage.py createsuperuser
   ```

4. Start the development server:

   ```powershell
   .\.venv\Scripts\python.exe manage.py runserver
   ```
