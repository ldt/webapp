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
- UV for dependency management (https://github.com/astral-sh/uv)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/webapp.git
   cd webapp
   ```

2. Install dependencies:
   ```bash
   pip install uv
   uv sync --dev
   ```

3. Set up environment variables (see `.env.example` for reference):
   ```bash
   cp .env.example .env
   # Edit the .env file with your configuration
   ```

4. Run database migrations:
   ```bash
   uv run alembic upgrade head
   ```

5. Start the development server:
   ```bash
   uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 52485
   ```

6. Open your browser and navigate to http://localhost:52485

## Running Tests

### Unit Tests

```bash
uv run pytest
```

### End-to-End Tests

```bash
playwright install
uv run pytest e2e/
```