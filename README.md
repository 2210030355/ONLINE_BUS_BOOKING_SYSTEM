# README

## Online Bus Booking System

This project is an **Online Bus Booking System** built using Django and Flask. It allows users to search, book, and manage bus tickets through a web interface. The application uses Django for the backend and Flask for specific microservices.

---

## Features
- User authentication and profile management.
- Search and filter buses by date, destination, and timing.
- Book tickets and manage reservations.
- Admin panel to manage bus schedules, routes, and user data.
- Microservices for handling payment processing using Flask.

---

## Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Django 3.x+
- Flask 2.x+

---

## Setup Instructions

### 1. Clone the Repository
```bash
# Clone this repository
git clone https://github.com/your-username/online-bus-booking-system.git
cd online-bus-booking-system
```

### 2. Set Up Virtual Environment
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install required Python packages
pip install -r requirements.txt
```

### 4. Configure the Database
- Update the `settings.py` file in the Django project with your database credentials.
- Run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### 5. Start the Flask Microservice
- Navigate to the `flask_service` directory:
  ```bash
  cd flask_service
  python app.py
  ```

### 6. Start the Django Application
- Return to the main project directory and run the Django server:
  ```bash
  python manage.py runserver
  ```

### 7. Access the Application
- Open your web browser and go to:
  ```
  http://127.0.0.1:8000
  ```

---

## File Structure
```
online-bus-booking-system/
├── django_project/        # Main Django project
├── flask_service/         # Flask microservice for payments
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, Images)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## Dependencies
- Django
- Flask
- SQLite (default database)
- Gunicorn (for production deployment)

---

## Deployment
### Using Docker
- Build and run the containers:
  ```bash
  docker-compose up --build
  ```
- The Django application will run on `http://127.0.0.1:8000` and Flask on the specified port.


---

## Thank You
For any issues or suggestions, please raise a GitHub issue in this repository.
