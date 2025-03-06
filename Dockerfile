# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev curl

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Django
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for Django development server
EXPOSE 8000

# Command to run the application (use `runserver` in dev, or `gunicorn` for production)
CMD ["python", "blog_heho/manage.py", "runserver", "0.0.0.0:8000"]
