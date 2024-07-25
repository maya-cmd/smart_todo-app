TaskZen

Table of Contents
Introduction
Features
Technologies Used
Installation
Usage
Deployment
Contributing
License
Contact
Introduction
TaskZen is a smart to-do list application designed to help users organize, prioritize, and complete their tasks efficiently. The app aims to enhance productivity by providing a seamless and intuitive task management experience.

Features
Task Management: Add, update, and delete tasks.
Task Status: Mark tasks as accomplished or not accomplished.
Responsive Design: Compatible with both web and mobile devices for a consistent user experience.
Custom Thank You Page: Users are redirected to a custom thank you page after completing tasks.
Technologies Used
Frontend:
HTML5
CSS3
JavaScript (Vanilla)
Backend:
Python
Flask
Database:
PostgreSQL (for production on Heroku)
MySQL (for local development)
Hosting:
Heroku
Installation
Prerequisites
Python 3.8+
MySQL (for local development)
PostgreSQL (for production)
Git
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/taskzen.git
cd taskzen
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

MySQL (Local Development):

sql
Copy code
CREATE DATABASE taskzen;
Update the database configuration in config.py:

python
Copy code
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/taskzen'
PostgreSQL (Production):

Heroku provides the PostgreSQL database, and its configuration will be handled automatically.

Run the application:

bash
Copy code
flask run
Usage
Home Page: Includes a custom landing page with a welcoming message and navigation buttons.
My List: Allows users to add, view, update, and delete tasks.
About: Provides information about the application and its purpose.
Deployment
Heroku
Login to Heroku:

bash
Copy code
heroku login
Create a new Heroku app:

bash
Copy code
heroku create taskzen
Push the code to Heroku:

bash
Copy code
git push heroku main
Set up the PostgreSQL add-on:

bash
Copy code
heroku addons:create heroku-postgresql:hobby-dev
Run migrations to set up the database:

bash
Copy code
heroku run flask db upgrade
Open the app in your browser:

bash
Copy code
heroku open
