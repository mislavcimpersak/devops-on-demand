# DevOps On Demand

[![CircleCI](https://circleci.com/gh/mislavcimpersak/devops-on-demand/tree/master.svg?style=svg)](https://circleci.com/gh/mislavcimpersak/devops-on-demand/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/mislavcimpersak/devops-on-demand/badge.svg?branch=master)](https://coveralls.io/github/mislavcimpersak/devops-on-demand?branch=master)

A Django exercise.

Calculates optimal number of DevOps Managers and DevOps Engineers required to cover multiple data centers.
Servers are maintained by the DevOps Manager and possibly other DevOps Engineers called in on-demand. There is only one Manager, but there can be many Engineers.

## Notes

### Running the Project Locally

1. Make a new Python 3.6 virtual environment
2. Install dependencies: `pip install -r requirements/dev.txt`
3. Run app: `python manage.py runserver`
4. API endpoint is available at `http://127.0.0.1:8000`

### Framework and Tools Used

Django and Django Rest Framework are a total _overkill_ for this kind of exercise. Oh, well :)
In real life situation Falcon/Hug/API Star would be a better fit for this case.

### Pre-commit Hooks

Project uses [pre-commit](https://github.com/pre-commit/pre-commit) hooks. To use them for your local development install them with the following command:

```
pre-commit install
```

Code formating is done with [Black](https://github.com/ambv/black) and an additional [requirement files check](https://github.com/pre-commit/pre-commit-hooks) is run.

### Django Configuration

Again, using [Django-Configurations](https://github.com/jazzband/django-configurations) is a total overkill for this project, but is a smart thing to use in a project from the beginning if it ever grows (ok, this one won't 😇 ).

To ease first time run, by default development config (`devops_on_demand.settings.DevConfig`) will be used.

### `.env` file

Another overkill: [Django-environ](https://github.com/joke2k/django-environ/), but a smart practice.

All required environment variables for the project are available in `.env` file.
`.env` file is included in this repo, but in a real life scenario this file should not be commited to VCS. It is commited in this repo to get the person who is running the code in front of a working project as soon as possible.

### Tests

Whole code is covered with tests and additional acceptance tests are in `maintenance/tests/test_exercise_acceptance.py`.

#### pytest

[pytest](https://docs.pytest.org/en/latest/) is used for running the test suite. Position yourself in the root of the project and just run:

```
pytest
```

[Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/) report is available on run.

#### Test using curl

Run the project locally and fire up curl from the shell:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"DM_capacity": "20", "DE_capacity": "8", "data_centers": [{"name": "Paris", "servers": "20"}, {"name": "Stockholm", "servers": "62"}]}' \
  http://127.0.0.1:8000/

```
