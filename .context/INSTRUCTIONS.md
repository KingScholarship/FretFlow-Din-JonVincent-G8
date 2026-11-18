## TECHNOLOGY STACK (required)

- Full Stack Django (Django handles both the backend and the frontend through Django templates)
- Database: PostgreSQL or Supabase (Supabase uses PostgreSQL)
- Do not use SQLite for your final setup.

## REQUIRED FEATURE: ACCOUNT FEATURE

### Account Registration
- Users can create an account through a registration form.
- Validate the input: required fields, a valid email format, a unique username/email, and a password confirmation that matches.
- Passwords must be hashed. Use Django’s built-in authentication; never store plain-text passwords.
- Show clear success and error messages.

### Login / Logout
- Registered users can log in with their credentials.
- Show an error message when the credentials are invalid.
- Users can log out, which ends their session.
- Protect pages that need a logged-in user (for example, with @login_required). A logged-out user who tries to open them should be sent to the login page.
### Role-Based User Dashboard
- Your system must have at least two user roles that fit your project (for example, Admin and Customer, or Staff and Member).
- After logging in, each user goes to the dashboard for their role.
- Each dashboard shows content and navigation that fit that role.
- A user must not be able to open another role’s dashboard by typing its URL.
### User Profile
- Logged-in users can view their profile information.
- Users can update their profile details (for example, name, email, contact number, or profile photo).
- Users can only view and edit their own profile.

## GITHUB REPOSITORY REQUIREMENTS

Repository name format: SystemName-Lastname-Firstname-Section
Example: GreenLeaf-DelaCruz-Juan-G01
Set the repository to Public.
Commit and push your work regularly. Your commit history should show your progress over time, not one upload at the end.
Do not push secrets. Keep your database credentials and Supabase keys in a .env file and add .env to .gitignore. Also exclude your virtual environment folder (venv/) and pycache/.
Include a requirements.txt file.

## Project Flow
- Create a flow for the project in tables, containing the status of each app.
- Make sure that I only need to say continue every after creation.
- e.g. accounts app is completed, then you commit and push using [GITHUB.md](GITHUB.md) instructions
- Then after that ask the user to continue to keep doing whats left.

---

# IMPORTANT!!!
- ### Do not overengineer everything
- ### My project is too complex, make sure to simplify the web app
- ### You can be as creative as you want when designing the templates using the Official Django Coding Style
