from python:3.9

workdir /app

run pip install django

add . /app

ENTRYPOINT [ "python", "/app/manage.py", "runserver", "0.0.0.0:80" ]