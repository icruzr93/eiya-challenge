# Fibonacci Calculator

This application was made with django restframework, postgresql, nginx, react, docker and docker compose.

## Run Project

### Development

```sh
docker-compose up -d --build
```

## Reviewing Client

Go to http://localhost and enter a number on header section where the app will be automatically updated once you click enter, besides that the app auto updates each 5 seconds.

## Reviewing API

Go to http://localhost/api/records/ to create records or to list all the records (GET, POST)

Or to http://localhost/api/records/:id to get, update or delete a specific record

### Testing

```sh
docker-compose up -d --build
docker-compose exec api python manage.py test
```
