FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# Creating working directory
RUN mkdir -p /app
WORKDIR /app

# Copying requirements
COPY requirements.txt .
COPY requirements/ /app/requirements/

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

COPY docker-entrypoint.sh /app

COPY ./src/ ./src

RUN mkdir -p /app/src/static/

EXPOSE 8000

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
