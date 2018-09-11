# DevOps On Demand

A Django exercise.

## Notes

### Running the Project Locally

1. Make a new Python 3.6 virtual environment
2. Install dependencies: `pip install -r requirements/dev.txt`
3. Run app: `python manage.py runserver`

### Pre-commit Hooks

Project uses [pre-commit](https://github.com/pre-commit/pre-commit) hooks. To use them for your local development install them with the following command:

```
pre-commit install
```

### Django Configuration

To ease first time run, by default development config (`devops_on_demand.settings.DevConfig`) will be used.

### `.env` file

All required environment variables for the project are available in `.env` file.
`.env` file is included in this repo, but in a real life scenario this file should not be commited to VCS. It is commited in this repo to get the person who is running the code in front of a working project as soon as possible.
