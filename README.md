# NudgeMe

## Installation Guide

Follow these steps to set up and run the project:

### 1. Clone the Project
Clone the repository from GitHub:
```sh
git clone <repository_url>
```

### 2. Navigate into the project directory
```sh
cd NudgeMe
```

### 3. Build and start the containers
```sh
docker compose up -d --build
```

### 4. Apply the migrations
```sh
docker exec nudgeme_app ./manage.py shell -c 'from django.conf import settings;apps =[app.split(".")[-1] for app in settings.INSTALLED_APPS]; print(" ".join(apps))' | xargs docker exec nudgeme_app ./manage.py makemigrations
docker exec nudgeme_app ./manage.py migrate
```

### 5. Create a superuser.
```sh
docker exec nugdeme_app ./manage.py createsuperuser
```

### 6. Access the swagger.
The swagger page of the API can be accessed through
`http://localhost:8654/api/meta/swagger`
