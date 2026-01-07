# Flask-Web-Application-with-SQL-Integration

This guide provides an introductory walkthrough on managing forms, connecting to a database, and performing SQL operations within a Flask web application on an Amazon Linux 2023 EC2 instance.

![Databases in Flask](./database.png)

## Learning Goals

By following this tutorial, you will be able to:

* Set up Python and the Flask framework on an Amazon Linux 2023 EC2 instance.
* Develop a web application using Python and Flask.
* Manage web forms using the `flask-wtf` library.
* Connect and configure a `SQLite` database.
* Connect and configure a `MySQL` database.
* Execute SQL queries within a Flask application.
* Use Git to control versions of your application.
* Deploy and run the web application on an EC2 instance using GitHub as the code source.

## Expected Tasks

* Review and run the `app-with-sqlite.py` script.
* Create `app-with-mysql.py` in the same directory and adjust it to connect with a MySQL RDS database.

## Tutorial Outline

* **Step 1**: Run the sample web app using SQLite and inspect the database implementation.
* **Step 2**: Rewrite the application to use MySQL.
* **Step 3**: Install Python and Flask on Amazon Linux 2023 EC2 and run the MySQL version.

## Step 1: Explore and Run the SQLite Example

* Identify the modules imported in the project.
* Review the database setup in `app-with-sqlite.py`:

```
- Sets necessary environment variables for SQLite as per documentation:
   https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
- Drops the `users` table if it exists, creates a new one, and inserts sample data.
- Executes SQL commands to populate the database.
```

* Understand the functions:

```
- `find_emails`: Searches for emails using a username keyword and returns `(name, email)` tuples.
- `insert_email`: Adds a new email entry to the `users` table.
```

* Review Flask routes:

```
- `/`: Searches emails by keyword using GET and POST, uses `emails.html` template.
- `/add`: Adds new emails using GET and POST, uses `add-email.html` template.
- The Flask app listens on port 8080 for all hosts.
```

* Ensure required packages are installed: `flask-mysql`, `sqlalchemy`, `Flask-SQLAlchemy`.
* Run the app using `app-with-sqlite.py`.
* Inspect database tables with SQLite Browser: [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

## Step 2: Configure and Run MySQL Version

* Set up an RDS MySQL database with these options:

```
- Engine: MySQL 8.0.35
- Template: Free tier
- Instance class: db.t2.micro
- Public access: Yes
- Master username: admin
- Master password: Sule_1
- Initial database name: sule
```

* Create `app-with-mysql.py` in the same folder as the SQLite app.
* Adjust the configuration to use the RDS MySQL database.
* Refer to the environment variable documentation: [https://flask-mysql.readthedocs.io/en/stable/](https://flask-mysql.readthedocs.io/en/stable/)
* Commit changes and push to GitHub.
* Launch an EC2 instance and pull your project files.

## Step 3: Install Python and Flask on Amazon Linux 2023 EC2

* Launch an EC2 instance with Amazon Linux 2023 AMI, enabling SSH (port 22) and HTTP (port 8080).
* Connect via SSH.
* Update packages and cache.
* Install Python 3 and pip3.
* Verify versions of Python and pip.
* Install Flask version 2.3.3 to avoid compatibility issues: `pip install Flask==2.3.3`.
* Install `flask_mysql`.
* Run the Flask application with Python.
