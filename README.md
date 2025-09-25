# alx-project-nexus

![Built with Django](https://img.shields.io/badge/Built%20with-Django-blue.svg)

This repository contains the backend source code for a robust Online Poll System, built with Python and the Django REST Framework. It provides a full-featured RESTful API for user registration, authentication, and managing polls with a secure, real-time voting system.

The live API and its interactive documentation are available at **[alx-project-nexus](https://alx-project-nexus-fixq.onrender.com)**.

---

## Key Features

- **User Authentication**: Secure user registration and login using JSON Web Tokens (JWT).
- **Poll Management**: Authenticated users can create polls with multiple choices and optional expiry dates.
- **Secure Voting System**: Users can vote on polls, with backend validation to prevent duplicate votes.
- **Real-Time Results**: An endpoint to fetch real-time results, including total vote counts and the percentage for each choice.
- **Interactive API Documentation**: Automatically generated, interactive API documentation using Swagger (OpenAPI) for easy testing and exploration.

---

## API Endpoints

The base URL for the API is `/api/`. The full, interactive documentation can be found at `/api/docs/`.

| Method | Endpoint                   | Description                               | Requires Auth |
| :----- | :------------------------- | :---------------------------------------- | :------------ |
| `POST` | `/api/register/`           | Create a new user account.                | No            |
| `POST` | `/api/token/`              | Log in to get a JWT access/refresh token. | No            |
| `GET`  | `/api/polls/`              | Get a list of all polls.                  | No            |
| `POST` | `/api/polls/`              | Create a new poll.                        | Yes           |
| `GET`  | `/api/polls/<id>/`         | Get the details of a single poll.         | No            |
| `POST` | `/api/polls/<id>/vote/`    | Cast a vote on a specific poll.           | Yes           |
| `GET`  | `/api/polls/<id>/results/` | Get the vote counts for a specific poll.  | No            |

---

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: djangorestframework-simplejwt (JWT)
- **API Documentation**: drf-yasg (Swagger)
- **Deployment**: Gunicorn, Render

---

## Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/Nissau96/alx-project-nexus.git](https://github.com/Nissau96/alx-project-nexus.git)
    cd alx-project-nexus
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a `.env` file in the root directory and add your secret key. You can generate a new one if needed.

    ```env
    SECRET_KEY=your-super-secret-key-here
    DEBUG=True
    ```

5.  **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000`.
