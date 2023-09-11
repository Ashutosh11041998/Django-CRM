# CRM Project README

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Authentication](#authentication)
- [Database](#database)
- [Frontend](#frontend)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Welcome to the CRM (Customer Relationship Management) project built using Django and MySQL. This CRM system allows users to manage customer information, including creating, reading, updating, and deleting customer records. User authentication is integrated to ensure data security, and Bootstrap is used for the frontend to enhance the user experience.

## Features
- User Authentication: Secure user accounts with registration and login functionality.
- Create: Add new customer records with details such as name, contact information, and notes.
- Read: View a list of all customer records and click to see individual details.
- Update: Edit customer information and save changes.
- Delete: Remove customer records, but only the user who created a record can delete it.
- Responsive UI: Utilizes Bootstrap for a user-friendly and mobile-responsive interface.

## Requirements
To run this CRM project, ensure you have the following software installed on your system:

- Python (3.7+)
- Django (3.0+)
- MySQL

## Installation
Follow these steps to set up the CRM project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crm-project.git
   cd crm-project
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a MySQL database for the project and update the database configuration in `settings.py`.

5. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
Access the CRM application by opening a web browser and navigating to `http://localhost:8000/`. You can log in using the superuser account or create new user accounts for your team members. Once logged in, you can perform the CRUD operations on customer records.

## Authentication
User authentication is integrated into the CRM project. Users can register their accounts or log in if they already have one. Only authenticated users can access and manage customer information.

## Database
This CRM project uses a MySQL database to store customer data. You can configure the database connection in the `settings.py` file.

## Frontend
The frontend of the CRM project is built using Bootstrap to ensure a clean and responsive user interface. You can further customize the frontend by modifying the templates and static files located in the `templates` and `static` directories.

## Contributing
If you'd like to contribute to this project, please follow the standard open-source guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Create a pull request with a clear description of your changes.

## License
This CRM project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of this license.
