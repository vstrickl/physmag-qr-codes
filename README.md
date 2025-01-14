# QR Code App Django Backend

This repository contains the backend for a QR code application built with Django. The backend serves as the database managing QR code generation, storage, and retrieval. It is containerized using Docker for seamless deployment and scalability.

## Features

- **Dynamic QR Code Generation**: Dynamically generates QR codes based on user input or predefined templates.
- **Database Integration**: Manages QR code data using a relational database.
- **Dockerized Deployment**: The backend is fully containerized with Docker for consistency and scalability.


## Tech Stack

- **Backend Framework**: Django
- **API Framework**: Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Containerization**: Docker

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (>=3.8)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd physmagQRCodes
   ```

2. Run database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the app for local testing:
   ```bash
   commands/run_local
   ```

4. Access the Administration panel at `http://localhost:8000/admin/`.

### Configuration
Environment Variables: Set up environment variables for sensitive configurations (e.g., database credentials, secret key) using a .env file. Use the provided template.env file as a guide. Example:
   ```.env
   SECRET_KEY=your-secret-key
   DJANGO_ALLOWED_HOSTS=host.com.localhost
   DEBUG=True  # Set to False in production

   DBNAME=dbname
   DBHOST=dbhost
   DBPWD=dbpwd
   DBPORT=port
   DBUSER=dbuser
   ```

## Development

### Folder Structure

   ```plaintext
   app/
   ├── qr_codes             # App for managing QR codes
   │   ├── migrations       # Database migrations
   │   ├── serializers.py   # API serializers
   │   ├── models.py        # Database models
   │   ├── views.py         # API views
   ├── physmagQRCodes       # Django project folder
   │   ├── settings.py      # Project settings
   │   ├── urls.py          # Project URL configurations
   ├── Dockerfile           # Docker configuration
   ├── requirements.txt     # Python dependencies
   ├── manage.py            # Django management script
   ```

### Testing
Run the test suite:
   ```bash
   sdlc/tests
   ```

## Deployment
To deploy the Dockerized Django backend:

Build and push the image to GitHub. GitHub Actions will handle the deployment of the app to the Docker registry.

Deploy the container on your preferred platform (e.g., AWS, GCP, Heroku, etc.).

## License
This project is licensed under the [MIT License]().

For questions or contributions, please contact [Vonique Stricklen](vstrickl.git@gmail.com).
