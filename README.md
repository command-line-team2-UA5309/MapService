# Map Service

A microservice for managing map sightings.

## Features

- Create, list, and delete map sightings
- Sighting confirmation workflow
- Role-based permissions
- JWT authentication

## Quick Start

## Run locally

1. Create virtual environment and install dependencies:
`python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`.

2. Configure the `.env` file.

3. If you changed models.py, make migrations:
`python manage.py makemigrations`

4. Run migrations and start the server:
`python manage.py migrate`,
`python manage.py runserver`

## How to set up pre-commit hooks

1. Install pre-commit from <https://pre-commit.com/#install>
2. Run `pre-commit install`
3. Auto-update the config to the latest version `pre-commit autoupdate`
