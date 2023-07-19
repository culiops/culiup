# Culiup
![Testing](https://github.com/culiops/culiup/actions/workflows/testing.yml/badge.svg)

A free and open source uptime monitoring tool to help sysadmin, DevOps, SRE, and Cloud Engineer to have a better life

## The features
- Monitoring website
- Monitoring SSL
- Monitoring Port
- Monitoring Ping
- Status Page
- Incident and SLA reports


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