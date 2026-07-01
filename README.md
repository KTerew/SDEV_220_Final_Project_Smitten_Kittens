# Smitten Kittens

Smitten Kittens is a Django web application that helps users create listings for kittens that need new homes. Users can create listings and add one or more kittens with information such as name, description, and availability.

## Technologies

- Python
- Django
- SQLite


## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
```bash
pip install -r requirements.txt
```
4. Apply migrations.
```bash
python manage.py migrate
```
5. Create a superuser.
```bash
python manage.py createsuperuser
```
6. Start the development server.
```bash
python manage.py runserver
```
7. Open your browser and go to:
```
http://127.0.0.1:8000/
```
## Project Structure

- `SmittenKittens/` – Django project files
- `kittens/` – Application containing models
- `db.sqlite3` – SQLite database

## Features

- User accounts
- Create listings
- Add kittens to listings
- Django admin interface