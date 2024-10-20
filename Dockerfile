# Use this Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1         # Ensure stdout and stderr are unbuffered

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Change the working directory to the Django project root
WORKDIR /app/casseroleapi

# Run database migrations
RUN python manage.py migrate

# Command to run the app

CMD ["gunicorn", "casseroleapi.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1"]