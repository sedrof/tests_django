# helpcenter-fe

## [Development Environment] Docker build and project startup
```
docker-compose up --build
```

## [Production Environment] Docker build and project startup
```
docker-compose docker-compose.prod.yml up --build
```

### [Development Environment] Execute Django commands
```
docker-compose exec web python 'django commands' for example:
docker-compose exec web python manage.py migrate
```

### [Production Environment] Execute Django commands
```
docker-compose docker-compose.prod.yml exec web python 'django commands' for example:
docker-compose docker-compose.prod.yml exec web python manage.py migrate
```