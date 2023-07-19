FROM python:3-alpine

RUN apk add --no-cache curl openssh git musl-dev gcc libffi-dev python3-dev postgresql-dev jpeg-dev openssl \
              zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir --upgrade

ADD dockers/scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh