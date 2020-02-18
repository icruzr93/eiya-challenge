# Fibonnaci Calculator

This application was made with django restframework, postgresql, nginx, react, docker and docker compose.

## Reviewing API

Go To http://localhost/api/records/ to create records or to list all the records (GET, POST)
Or To http://localhost/api/records/:id to get, update or delete a specific record

## Running Project

### Development

```sh
docker-compose up -d --build
```

### Testing

```sh
docker-compose up -d --build
docker-compose exec api python manage.py test
```
