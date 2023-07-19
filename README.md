# Culiops
![Testing](https://github.com/culiops/culiops/actions/workflows/testing.yml/badge.svg)

An internal developer platform(IDP) to help sysadmin, DevOps, SRE, and Cloud Engineer to have a better life

## The features
- Monitoring cloud resources
- Monitoring cloud cost
- Monitoring endpoint
- Internal developer platform

## Development setup

### Create and active virtual environment
```
python -m venv venv
source venv/bin/activate
```
### Install the dependent packages
```shell
pip install -r requirements.txt
```

### Database setup
```shell
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py makemigrations
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py migrate
```

### Create admin user
```
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py createsuperuser --username=root --email=root@culiops.dev
```

### Run server
```
python manage.py runserver
```

### Run tests
```
python manage.py test --settings settings.base
```