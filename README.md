# Student Management System

Name: Ahmad El Mokahal

ID: 300059298

## Folder Structure
- `manage.py`: Entry point of the application.
- `student_management`: Main application directory.
- `students`: Application for managing all views related to students.

A detailed report explaining the design and implementation of the system has been provided in the repository as `A2_Report.pdf`. You may also access the report via the following [Google Docs link](https://docs.google.com/document/d/1xD2G91LYNUMriVieDLKFT5pmdUEShC4xPIiQjz8Yqmg/edit?usp=sharing).

## How to Run

First ensure that you have a version of Django installed, to install:

`python -m pip install Django`


Before you run the application for the first time, execute the following command:

`python manage.py migrate`


To run the application:

`python manage.py runserver`

Account credentials for testing:

  -- username: `admin`

  -- password: `admin123`

**NOTE:** To perform operations such as adding, deleting, updating student records, you must be signed in using the admin account credentials.