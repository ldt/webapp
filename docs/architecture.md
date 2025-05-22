# Architecture

This document describes the architecture of the web application.

## Overview

The application is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Project Structure

The project follows a modular structure with the following main directories:

- `app/`: Contains the main application code
  - `api/`: API routes and handlers
    - `routers/`: Contains the application routers
  - `core/`: Core functionality (config, auth, etc.)
  - `db/`: Database models and session management
  - `models/`: SQLAlchemy database models
- `docs/`: Markdown documentation files
- `templates/`: Jinja2 HTML templates
- `tests/`: Unit tests using pytest
- `e2e/`: End-to-end tests using Playwright

## Dependencies

The application uses the following main dependencies:

- FastAPI: Web framework
- Jinja2: Templating engine for HTML
- HTMX: JavaScript library for AJAX calls
- FastAPI-Users: User management package
- SQLAlchemy: ORM for database interactions
- PostgreSQL: Database

## Authentication and Authorization

The application uses JWT (JSON Web Tokens) for authentication. The tokens are stored in cookies.

## Database

The application uses PostgreSQL as the database, with SQLAlchemy for ORM.