# Technical Blog Platform

A blog platform built with Python and the Django framework, designed to share technical blog posts on various topics.

## Features

- Create and manage blog posts.
- User-friendly admin interface for content management.
- Easy setup with Django.
- Support Markdown language for blog content

## Create PostgreSQL Database

1. Create a new database in PostgreSQL.
```bash
sudo -u postgres psql
```

Adapt the config to match your settings
```sql
CREATE DATABASE mydb;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```


## Create .env file
Expected configuration in the .env file :
```text
# Looking to send emails in production? Check out our Email API/SMTP product!
EMAIL_HOST = '<host>' # e.g 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '<host_user>>'
EMAIL_HOST_PASSWORD = '<host_password>'
EMAIL_PORT = '2525'

# Setting PostgreSQL connection
DB_NAME = '<db_name>'
DB_USER = '<user>'
DB_PASSWORD = '<password>'
DB_HOST = '<ip>'
DB_PORT = '5432' # default postgres port
```

## Installation
 
1. Clone the repository:
   ```bash
   git clone git@github.com:maishuji/tech_blog_heho.git
   ```
2. Activate python environment (optional)
   ```bash
   source <path-to-env>/bin/activate
   ```
4. Install requirements
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations
   Be sure to configure your database settings in settings.py before running migrations
   ```bash
   python3 manage.py migrate
   ```
   You can check that the connection is working by running:
   ```bash
   python3 manage.py dbshell
   ```
   It should open a PostgreSQL shell if everything is configured correctly.
6. Create superuser
   ```bash
   python3 manage.py createsuperuser
   ```
7. Run server
   ```bash
   python3 manage.py runserver
   ```
