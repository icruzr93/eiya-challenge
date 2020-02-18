# Fibonnaci Calculator

This application was made with django restframework, postgresql, nginx, react, docker and docker compose.

## Run Project

### Development

```sh
docker-compose up -d --build
```

## Reviewing Client

Go To http://localhost and enter

## Reviewing API

Go To http://localhost/api/records/ to create records or to list all the records (GET, POST)

Or To http://localhost/api/records/:id to get, update or delete a specific record

### Testing

```sh
docker-compose up -d --build
docker-compose exec api python manage.py test
```
