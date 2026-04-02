# Speedcube Algorithm trainer (Django Project)
Author: Novikov Stanislav. MIPT 5th grade (1st year Master). Group: "М02-501"

## Project Description
A web application designed for speedcubers to track, learn and manage algorithm sets (e.g., CLL, EG-1, Square-1 CSP).

## Features Included
- Responsive grid and list layout for algorithm sets
- User uploaded images for better (personified) case recognition
- Sorting by name, date and learning status
- Ability to add user's own algorithms or cases, which can be put into existing or custom group

## How to run locally

1) Clone the repository
2) Create and activate virtual environment (python -m venv venv && source venv/bin/activate)
3) Install required libraries (pip install django Pillow)
4) To run use this command in order:

- python manage.py migrate
- python manage.py runserver

5) Open address, which pop-ups in terminal, in your browser

