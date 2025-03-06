# Use a lightweight version of Python to minimize image size
FROM python:3.9-slim  

# Set the working directory inside the container
WORKDIR /usr/src/app  

# Systemabhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the working directory
COPY requirements.txt .  

# Upgrade pip and install Python dependencies
RUN pip install -r requirements.txt  

# Copy the entire project to the container
COPY . . 

# Collect static files for production
RUN python manage.py collectstatic --noinput  

RUN pip install gunicorn

# Open port 8000 for the application
EXPOSE 8000  

# Set the default command to run Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
