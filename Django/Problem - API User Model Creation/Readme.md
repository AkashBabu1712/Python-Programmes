# Social Network API

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd social_network
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Apply migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Usage

- Access the API at `http://localhost:8000`
- Use the provided Postman collection to test the endpoints

## Endpoints

- Signup: `POST /signup/`
- Login: `POST /login/`
- Search Users: `GET /search/?search=<keyword>`
- Send Friend Request: `POST /friend-request/`
- Accept/Reject Friend Request: `PUT /friend-request/<id>/`
- List Friends: `GET /friends/`
- List Pending Friend Requests: `GET /pending-requests/`

