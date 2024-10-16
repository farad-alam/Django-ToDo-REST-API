# Django To-Do REST API

This is a To-Do application built using Django and Django REST Framework (DRF). The application allows users to manage their tasks efficiently, offering full CRUD (Create, Read, Update, Delete) functionality. Additionally, it includes features such as user authentication, task filtering, and sorting to enhance the user experience.

## Features

- User Registration, Login, and Authentication
- Create, Read, Update, and Delete tasks
- Task filtering and sorting by deadline, priority, and status
- Secure API endpoints with JWT (JSON Web Token) authentication
- API documentation using Swagger

## Technologies Used

- **Backend Framework**: Django
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite
- **Authentication**: JWT (JSON Web Token)
- **API Documentation**: Swagger / Postman

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- PostgreSQL
- Django
- Django REST Framework
- djangorestframework-simplejwt (for JWT authentication)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/farad-alam/Django-ToDo-REST-API.git
   cd Django-ToDo-REST-API
   ```
2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Set up PostgreSQL:**
Make sure PostgreSQL is running. Create a new database and configure the DATABASES setting in the settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


5. **Run migrations:**

```bash
python manage.py migrate
```
6. **Create a superuser (admin account):**

```bash
python manage.py createsuperuser
```

7. **Run the development server:**

```bash
python manage.py runserver
```

The project should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).



## API Endpoints

Below is an overview of the available API endpoints. You can test these using Postman or any API testing tool.

- **User Registration:** `POST /api/register/`
- **User Login:** `POST /api/login/`
- **Create a Task:** `POST /api/tasks/`
- **List Tasks:** `GET /api/tasks/`
- **Update a Task:** `PUT /api/tasks/<id>/`
- **Delete a Task:** `DELETE /api/tasks/<id>/`
- **Task Filtering and Sorting:** You can filter and sort tasks by deadline, priority, and status via query parameters.

## API Documentation

To view the API documentation, navigate to `/swagger/` on your local development server (i.e., [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)).

## Authentication

The API uses JWT for user authentication. To access protected routes, you will need to authenticate by obtaining a token via the login route:

- **Login Endpoint:** `/api/login/`
- **Token Refresh Endpoint:** `/api/token/refresh/`

Include the token in your headers for authenticated requests:

```bash
     Authorization: Bearer <your-token>
```
## Deployment
For deployment, you can follow these steps:

- Set up your production environment (e.g., Heroku, AWS, DigitalOcean).

- Ensure your environment variables (e.g., SECRET_KEY, DATABASE_URL, etc.) are correctly configured.

- Run the following commands to collect static files and apply migrations:

```bash
python manage.py collectstatic
python manage.py migrate
```
- Start your application using your preferred method (e.g., Gunicorn for Heroku or other hosting services).

## Project Structure
```bash

Django-ToDo-REST-API/
│
├── accounts/               # App containing Users
├── app/                    # App containing Tasks 
├── todo/                   # Main Django project directory
├── manage.py               # Django management script
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
### Farad Alam Foisal
GitHub: [@farad-alam](https://github.com/farad-alam)

LinkedIn: [Farad Alam](https://www.linkedin.com/in/farad-alam-foisal/)

## Contributions
Contributions are welcome! If you'd like to improve this project, please submit a pull request or open an issue on GitHub.
