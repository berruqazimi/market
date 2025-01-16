 # 🧥 Second-Hand Clothes Marketplace

This is a Django-based web application that allows users to publish, update, and unpublish garments in a second-hand clothes marketplace. The application provides RESTful API endpoints for both public and authenticated users to interact with the garments.

## 📋 Features

### User Authentication:
- Users can register, log in, and authenticate using JWT tokens.
- Custom user model includes fields such as full name, address, and a publisher field for garment ownership.
- Authenticated users can interact with the marketplace to publish, update, or unpublish garments.

### Garment Management:
- **Publish Garment:** Authenticated users (publishers) can publish garments with details such as type, description, size, and price.
- **Update Garment:** Publishers can update the details of their published garments.
- **Unpublish Garment:** Publishers can unpublish their own garments. Unauthorized users cannot modify garments that they do not own.

### Public Endpoints:
- **View Garments:** Public users can list and view garment details without authentication.
- **Search Garments:** Garments can be filtered by type, size, price, and other parameters.

## 🛠️ Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:


git clone <repository-url>
cd /path/to/your/project

## 2. Create a .env File
Create a .env file to store sensitive configuration, including database credentials:


POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=your_db_name
PGADMIN_DEFAULT_EMAIL=your_pgadmin_email
PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password

## 3. Set Up PostgreSQL Database
Ensure your PostgreSQL container is running. If you're using Docker Compose:


docker-compose up -d db
Connect to the PostgreSQL container:


docker exec -it <your_postgres_container_name_or_id> psql -U postgres
Create the required database and user:


CREATE USER admin WITH PASSWORD 'adminpassword';
CREATE DATABASE marketplace;
GRANT ALL PRIVILEGES ON DATABASE marketplace TO admin;

## 4. Build and Start the Services
Build the Django application image and start all services:


docker-compose up --build

## 5. Create Django Superuser
To create a Django superuser, run:


docker-compose run dj python manage.py createsuperuser

## 6. Access the Services
Django Application: http://localhost:8000
pgAdmin Interface: http://localhost:8080
Credentials:

PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin

## 7. Stop the Services

To stop the services, run:
docker-compose down
