# Technical Blog Platform

A blog platform built with Python and the Django framework, designed to share technical blog posts on various topics.

## Features

- Create and manage blog posts.
- User-friendly admin interface for content management.
- Easy setup with Django.
- Support Markdown language for blog content
- Category management for posts.


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

## Installation (Development)
 
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
   python3 blog_heho/manage.py migrate
   ```
   You can check that the connection is working by running:
   ```bash
   python3 blog_heho/manage.py dbshell
   ```
   It should open a PostgreSQL shell if everything is configured correctly.
6. Create superuser
   ```bash
   python3 blog_heho/manage.py createsuperuser
   ```
7. Run server
   ```bash
   python3 blog_heho/manage.py runserver
   ```

## Deployment

Instead of running the application locally, you can deploy it using Docker and Docker-compose. To do so, follow these steps:

   1. Install Docker and Docker Compose
   2. Build the Docker image
   ```bash
   docker build -t django_app .
   ```
   3. Run Docker Compose
   ```bash
   docker-compose up -d
   ```

### Prerequisites on server

#### Install and set docker and docker-compose on server

```bash
sudo apt update
sudo apt install docker.io docker-compose
docker-compose --version
sudo usermod -aG docker ubuntu
```
#### Setting up environment variables

- Create or import the key pair to the server (public key in ~/.ssh/authorized_keys) from EC2 instance management console.
- Set up the environment variables inside the instance in ~/.profile
<your-public-ip> : E.g. `www.mywebsite.com`
```bash
export DJANGO_ALLOWED_HOSTS='<your-public-ip>,<your-domain-name>'
export DJANGO_SECRET_KEY='<your-secret-key>'
export DJANGO_TRUSTED_HOSTS='<your-full-domain-name>' # Should start with https or http

# EMAIL CONFIGURATION
EMAIL_HOST = '<host>' # e.g 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '<host_user>>'
EMAIL_HOST_PASSWORD = '<host_password>'
EMAIL_PORT = '2525' # default mailtrap port
```

#### Setting up Nginx, and SSL certificate

#####  Install Nginx and Gunicorn
```bash
sudo apt install nginx
sudo apt install gunicorn
```
##### Configure Nginx with SSL certificate from Let's Encrypt (Free SSL Certificate)
```bash
sudo nano /etc/nginx/sites-available/tech_blog
```

######  Obtaining certificate from Let's Encrypt

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --standalone -d www.qcartier.dev
```

###### Add the following configuration at `/etc/nginx/sites-available/`

```text
server {
   listen 80;
   server_name <domain-name>; # E.g www.mynamewebsite.com

   # Redirect all HTTP traffic to HTTPS
   return 301 https://#host$request_uri;   
}

server {
    listen 443 ssl;
    server_name <domain-name>; # E.g www.mynamewebsite.com    

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/<domain-name>/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/<domain-name>/privkey.pem;

   # Serve statics in production (through https)
   location / {
      alias /var/www/static/
   }

    # Additional SSL settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';

    # HSTS Header for additional security
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Other server settings (e.g., Django app configuration)
    location / {
        proxy_pass http://localhost:8000;  # Adjust this if your app runs on a different port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## Troubleshooting

### Common Issues

#### Admin connection
You may need to create a superuser to access the Django admin interface.
For that, check the container `docker container ls`, go into the one running the Django app `docker exec -it <container_id> bash` and run the command to create the superuser:
```bash
python3 blog_heho/manage.py createsuperuser
```

#### Deploymnent failed

If for some reasons the deployment failed, remember to check the `disk usage` on the target machine. It is possible that the disk is full, which can cause the deployment to fail.

```bash
ssh ubuntu@<my_ip>
df -h
```

A `/dev/root` filesystem used at 100% would indicate a full disk. In this case, you need to free up space:

```bash
# Clean up unused docker images or containers
docker system prune -a

# Remove old logs or temporary files
sudo rm -rf /var/log/*
sudo rm -rf /tmp/*
```

### Error Server 500

If you encounter a 500 error, check the logs for more information. You can find the logs in the Nginx error log file:
```bash
sudo tail -f /var/log/nginx/error.log
```

#### Problem occuring only for certain pages

If this issue occurs only on some pages, it may be related to the database connection or a specific view in your Django application. For example, some pages use a model of field that is not present in the database.

This issue can occur when a change in a model has been recently made, but the database schema has not been updated accordingly. This can happen if you have added a new field to a model or changed the type of an existing field, but you have not run the necessary migrations to apply those changes to the database.
In this case, you may need to run migrations again:
```bash
python3 blog_heho/manage.py makemigrations
python3 blog_heho/manage.py migrate
```

If for some reason the migrations do not resolve the issue, and you see that the database is out of sync (e.g a field has not been added or removed), you can to try to manually update the schema. 
- It involves going into the db container, and run sql commands.
```sql
# Example of adding a column to a table
ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type>;
```


### Nginx not fetching the Django app

If you need to check the IP address of the container running the Django app, you can use the following command:
```text
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>
```

In the nginx configuration (likely `etc/nginx/sites-available/<name-of-the-site>`), you can use this IP address to set up the proxy_pass directive:
```text
proxy_pass http://<container_ip>:8000;
```

Restart Nginx to apply the changes:
```bash
sudo systemctl restart nginx
```

Verify the configuration
```bash
sudo systemctl status nginx
```


 

