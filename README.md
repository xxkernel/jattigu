# Fitness Application

A web application designed to help users create, manage, and follow personalized fitness training plans. This application allows users to track exercises, plan workouts, and monitor progress over time.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [DatabaseSchema](#database-schema)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [Members](#members)

## Features

- Create and manage exercise routines
- Set up personalized training plans
- Track progress with scheduled workouts
- Evaluate performance with calories burned and intensity levels
- User authentication and profile management

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL (or any other preferred database)
- HTML, CSS, JavaScript (Frontend)
- (Optional) Tailwind CSS for styling

## Installation

### Prerequisites

1. Python 3.8 or later
2. Django 4.0 or later
3. PostgreSQL (or preferred database)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/xxkernel/jattigu.git
   cd fitness-app
   ```
2. Create a virtual environment:

   ```bash
   python -m venv myvenv
   ```

3. Activate the virtual environment:

   On Windows:

   ```bash
   .\env\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source env/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply the migrations to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## DatabaseSchema

![Database Schema](frontend\public\jattigu_1.png)

## Endpoints

### General Endpoints

| Endpoint  | Method | Description     |
| --------- | ------ | --------------- |
| `/admin/` | GET    | Admin dashboard |
| `/`       | GET    | Home page       |
| `/about/` | GET    | About page      |

### Exercise Management Endpoints

| Endpoint                    | Method | Description                                   |
| --------------------------- | ------ | --------------------------------------------- |
| `/exercices/`               | GET    | Retrieves a list of all exercises             |
| `/exercice/<int:pk>/`       | GET    | Retrieves details of a specific exercise      |
| `/training-plans/`          | GET    | Retrieves a list of all training plans        |
| `/training-plans/<int:pk>/` | GET    | Retrieves details of a specific training plan |
| `/schedules/`               | GET    | Retrieves a list of all schedules             |

### Nutrition Management Endpoints

| Endpoint                | Method | Description                                        |
| ----------------------- | ------ | -------------------------------------------------- |
| `/categories/`          | GET    | Retrieves a list of all nutrition categories       |
| `/categories/<int:pk>/` | GET    | Retrieves details of a specific nutrition category |
| `/nutrition/`           | GET    | Retrieves a list of all nutrition items            |
| `/nutrition/<int:pk>/`  | GET    | Retrieves details of a specific nutrition item     |

### User Management Endpoints

| Endpoint         | Method | Description                                 |
| ---------------- | ------ | ------------------------------------------- |
| `/login/`        | POST   | Logs in a user                              |
| `/logout/`       | POST   | Logs out the current user                   |
| `/register/`     | POST   | Registers a new user                        |
| `/profile/`      | GET    | Retrieves the current user’s profile        |
| `/subscription/` | GET    | Retrieves subscription details for the user |

### Blog Management Endpoints

| Endpoint                     | Method | Description                                   |
| ---------------------------- | ------ | --------------------------------------------- |
| `/blog/`                     | GET    | Retrieves a list of all blog posts            |
| `/blog/<int:pk>/`            | GET    | Retrieves details of a specific blog post     |
| `/blog/create/`              | POST   | Creates a new blog post                       |
| `/blog/categories/`          | GET    | Retrieves a list of all blog categories       |
| `/blog/categories/<int:pk>/` | GET    | Retrieves details of a specific blog category |

## Members:

    * Abaizhanov Temirlan 22B030503
    * Shapkat Yernur 22B030465
    * Tasbay Akzhol 22B030592

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
