from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Create Flask app
app = Flask(__name__)

# MySQL RDS connection (your data)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Sule_1@sule.cbanmzptkrzf.us-east-1.rds.amazonaws.com:3306/sule'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create table and insert sample Sule data
with app.app_context():
    drop_table = text('DROP TABLE IF EXISTS users;')
    users_table = text(""" 
    CREATE TABLE users(
        username VARCHAR(50) NOT NULL PRIMARY KEY,
        email VARCHAR(50)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """)
    data = text("""
    INSERT INTO users (username, email)
    VALUES
        ('Sule1', 'sule1@example.com'),
        ('Sule2', 'sule2@example.com'),
        ('Sule3', 'sule3@example.com'),
        ('Sule4', 'sule4@example.com'),
        ('Sule5', 'sule5@example.com'),
        ('Sule6', 'sule6@example.com');
    """)
    db.session.execute(drop_table)
    db.session.execute(users_table)
    db.session.execute(data)
    db.session.commit()

# Function to find emails by keyword
def find_emails(keyword):
    with app.app_context():
        query = text(f"SELECT * FROM users WHERE username LIKE '%{keyword}%';")
        result = db.session.execute(query)
        user_emails = [(row[0], row[1]) for row in result]
        if not any(user_emails):
            user_emails = [("Not Found", "Not Found")]
        return user_emails

# Function to insert new email
def insert_email(name, email):
    with app.app_context():
        query = text(f"SELECT * FROM users WHERE username = '{name}'")
        result = db.session.execute(query)
        response = ''
        if len(name) == 0 or len(email) == 0:
            response = 'Username or email cannot be empty!'
        elif not any(result):
            insert = text(f"INSERT INTO users (username, email) VALUES ('{name}', '{email}');")
            db.session.execute(insert)
            db.session.commit()
            response = f"User {name} and {email} have been added successfully"
        else:
            response = f"User {name} already exists"
        return response

# Route: search emails
@app.route('/', methods=['GET', 'POST'])
def emails():
    with app.app_context():
        if request.method == 'POST':
            user_app_name = request.form['user_keyword']
            user_emails = find_emails(user_app_name)
            return render_template('emails.html', name_emails=user_emails, keyword=user_app_name, show_result=True)
        else:
            return render_template('emails.html', show_result=False)

# Route: add email
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    with app.app_context():
        if request.method == 'POST':
            user_app_name = request.form['username']
            user_app_email = request.form['useremail']
            result_app = insert_email(user_app_name, user_app_email)
            return render_template('add-email.html', result_html=result_app, show_result=True)
        else:
            return render_template('add-email.html', show_result=False)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
