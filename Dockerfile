FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update

COPY  requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Collect static files for production
RUN python manage.py collectstatic --noinput

RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application" ]






