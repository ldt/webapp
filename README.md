# Web App with FastAPI User Management

This is a web application built using FastAPI, Jinja2 templates, and HTMX for AJAX calls. It includes user management functionality using FastAPI-Users.

## Features

- User registration and login
- Password reset functionality
- Markdown documentation in the `/docs` folder
- Unit tests using pytest
- End-to-end tests using Playwright

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL database
- Poetry for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/webapp.git
   cd webapp
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up environment variables (see `.env.example` for reference):
   ```bash
   cp .env.example .env
   # Edit the .env file with your configuration
   ```

4. Run database migrations:
   ```bash
   poetry run alembic upgrade head
   ```

5. Start the development server:
   ```bash
   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 52485
   ```

6. Open your browser and navigate to http://localhost:52485

## Running Tests

### Unit Tests

```bash
poetry run pytest
```

### End-to-End Tests

```bash
poetry run playwright install
poetry run pytest e2e/
```