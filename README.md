# CuliUp
![Testing](https://github.com/culiops/culiup/actions/workflows/testing.yml/badge.svg)
![CodeQL](https://github.com/culiops/culiup/actions/workflows/github-code-scanning/codeql/badge.svg)
![Versions](https://img.shields.io/badge/python-3.8,%203.9,%203.10,%203.11-blue)
[![Repository License](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](LICENSE)

A free and open source uptime monitoring tool to help sysadmin, DevOps, SRE, and Cloud Engineer to have a better life

## The Feature
- Monitoring Website
- Monitoring SSL
- Monitoring Domain
- Monitoring Port
- Monitoring Ping
- Status Page
- Incident and SLA reports


## Development setup
### Your local - without Docker
*Create and active virtual environment*
```
python -m venv venv
source venv/bin/activate
```
*Install the dependent packages*
```shell
pip install -r requirements.txt
```

*Database setup*
```shell
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py makemigrations
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py migrate
```

*Create admin user*
```
DJANGO_SETTINGS_MODULE=settings.dev ./manage.py createsuperuser --username=root --email=root@culiup.xyz
```

*Run server*
```
python manage.py runserver
```
### With Docker
```
docker-compose up
```
## Testing
```
python manage.py test --settings settings.base
```