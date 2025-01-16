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

🚀 Usage
1. Key Pages

2. Admin Access
Admin Panel: http://localhost:8000/admin/ - Manage users, Garmnets

Obtain Token: http://localhost:8000/api/token/
Generate a JWT token by providing valid username and password.
Method: POST

Refresh Token: http://localhost:8000/api/token/refresh/
Refresh an expired JWT token.
Method: POST

Garment API
Garment List: http://localhost:8000/clothes/
View a list of all garments. Searchable by query parameters (e.g., cloth_type, size).
Method: GET

Publish Garment: http://localhost:8000/clothes/publish/
Allow authenticated users to publish a new garment using a form.
Method: GET, POST

Unpublish Garment: http://localhost:8000/clothes//unpublish/
Allow authenticated users to delete their own garments.
Method: DELETE

Update Garment: http://localhost:8000/clothes//update/
Allow authenticated users to update their own garments.
Method: PUT,PATCH

🧪 Testing
1. Run Tests
Tests are located in the tests folder. To run the tests:
docker ps -> id
docker exec -it marketplace-db-1 psql -U postgres
ALTER USER admin WITH CREATEDB;
\q exit

docker-compose run dj python manage.py test

2. Test Scenarios
test_publish_garment
Purpose: Verifies that an authenticated user can successfully publish a new garment.
Explanation: The test sends a POST request with garment details and ensures the response status is 201 Created, confirming the garment was published.

2. test_unpublish_garment
Purpose: Tests whether an authenticated user can unpublish (delete) a garment they own.
Explanation: The test sends a DELETE request for the garment and ensures the response status is 204 No Content, indicating successful deletion.

3. test_unpublish_garment_by_other_user
Purpose: Ensures that a user cannot unpublish a garment published by someone else.
Explanation: The test simulates another user attempting to delete the garment and expects a 403 Forbidden response, validating proper permission handling.

4. test_update_garment
Purpose: Confirms that an authenticated user can update the details of a garment they own.
Explanation: The test sends a PUT request with updated garment details and verifies a 200 OK response, ensuring the updates are applied successfully.

5. test_delete_garment_by_other_user
Purpose: Verifies that a user cannot delete a garment owned by another user.
Explanation: The test simulates another user attempting to delete the garment and expects a 403 Forbidden response, demonstrating proper access control.

📄 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

