# Math API Documentation

## Overview

The **Math API** is a RESTful API developed in Django that provides basic mathematical operations: **sum** and **average** of an integer vector. Additionally, the API logs the calculation history into a PostgreSQL database.

### Features
- **Sum**: Adds all numbers in an array.
- **Average**: Computes the arithmetic mean of the numbers in an array.
- **History**: Logs each operation with details such as operation type, input numbers, result, and timestamp.

## Requirements

- Python 3.8+
- Django 3.2+ and Django REST Framework
- Docker and Docker Compose (for PostgreSQL)
- PostgreSQL (running via Docker or installed locally)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/math_api.git
cd math_api
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration with Docker

To store calculation history, use Docker Compose to launch a PostgreSQL container. Ensure the following `docker-compose.yml` file is in the project root:

```yaml
version: '3'
services:
  postgres:
    image: postgres:13
    container_name: math_api_postgres
    restart: always
    environment:
      POSTGRES_DB: math_api_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass123
    ports:
      - "5432:5432"
```

### Start the Database Container

```bash
docker-compose up -d
```

## Django Configuration

Modify the `settings.py` file to configure PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'math_api_db',
        'USER': 'user',
        'PASSWORD': 'pass123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## API Documentation

### Endpoints

#### 1. Sum
**Endpoint:** `POST /api/calculator/sum/`

**Request Body (JSON):**

```json
{
  "numbers": [1, 2, 3, 4]
}
```

**Response (JSON):**

```json
{
  "result": 10
}
```

#### 2. Average
**Endpoint:** `POST /api/calculator/average/`

**Request Body (JSON):**

```json
{
  "numbers": [1, 2, 3, 4]
}
```

**Response (JSON):**

```json
{
  "result": 2.5
}
```

## Example Requests Using cURL

### Sum
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4]}' \
  http://localhost:8000/api/calculator/sum/
```

### Average
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4]}' \
  http://localhost:8000/api/calculator/average/
```

## Running Tests

Unit tests have been implemented for classes and endpoints. Run them using:

```bash
python manage.py test
```

