# Late Show Flask API

## Overview
This is a Flask API for the Late Show application that manages episodes and guest appearances. It provides endpoints to retrieve, create, and manage data related to show episodes and guest appearances.

## Requirements
To run this project, you'll need the following:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow

## Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/late-show-api.git
   cd late-show-api
Create and Activate a Virtual Environment:

```bash
Copy code
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install Requirements:

```bash
Copy code
pip install -r requirements.txt
Run the Application:

```bash
Copy code
python app.py
Seed the Database (if applicable):

```bash
Copy code
python seed.py
API Endpoints
Here are the available API endpoints:

GET /episodes: Retrieve all episodes.
GET /episodes/<id>: Retrieve a specific episode by ID.
GET /guests: Retrieve all guests.
POST /appearances: Create a new guest appearance.
#Database Initialization
To set up the database, follow these steps:

Initialize the Database: Open a Python shell or add the following code to your app.py to create the database:

python
Copy code
from app import db
db.create_all()
Run the Application: Start your Flask application:

```bash
Copy code
python app.py
Seed the Database: Populate your database with initial data from the CSV files:

```bash
Copy code
python seed.py
Testing
You can test the API endpoints using Postman. Import the provided Postman collection to facilitate testing of all available endpoints.

Final Steps
Make sure to run the application and seed the database as described above before testing.
Ensure the virtual environment is activated whenever you run the application or scripts.
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
