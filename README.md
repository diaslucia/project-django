<br />

# APPSchool

## 🔎 About

This website was developed using Python + Django.

## 🚀 Ejecution

Steps to install and run the project:

1. Clone the project
   ```sh
   git clone https://github.com/diaslucia/project-django.git
   ```
2. Open your current directory project
   ```sh
   cd project-django
   ```
3. Install
   ```sh
   pipenv install -r requirements.txt
   ```
4. Move to project folder

   ```sh
   cd project
   ```

5. Ejecute the app

   ```sh
   py manage.py runserver
   ```

## 🌐 URLS

- AppSchool: to visit the homepage
- AppSchool/courses: to access the list of courses and to be able to search an specific course
- AppSchool/formCourse: to add a new course
- AppSchool/students: to access the list of all students
- AppSchool/formStudent: to add a new student
- AppSchool/professors: to access the list of all professors
- AppSchool/formProfessor: to add a new professor

## 📂 Structure

The file structure is:

- AppSchool: to store python files that build the project.
- migrations: to store database migration files.
- static: to store assets like images, css and scripts.
- templates: to html files.

### Views File

- home: Renders the homepage.
- formCourse: Handles new course creation via a form.
- formStudent: Handles new student creation via a form.
- formProfessor: Handles new professor creation via a form.
- courses: Displays courses with a search form.
- students: Displays all students.
- professors: Displays all professors.

### Urls File

This file defines the URL patterns (routes) for a Django application, mapping specific URLs to corresponding views/functions, enabling access to different parts of the application: the home page, courses, student and professor creation forms, and lists of students and professors.

### Models File

This File defines three Django models named Course, Student, and Professor, each with specific fields, allowing the application to store and manage information about courses, students, and professors in a relational database.

### Forms File

The purpose of this file is to define Django form classes that specify the structure and validation rules for user input in the Django application.
