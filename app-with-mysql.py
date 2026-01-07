# Import Flask modules
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

# Create Flask app
app = Flask(__name__)

# Configure MySQL database
app.config['MYSQL_DATABASE_HOST'] = 'sule.cbanmzptkrzf.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Sule_1'
app.config['MYSQL_DATABASE_DB'] = 'sule'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Create users table and insert sample data
drop_table = 'DROP TABLE IF EXISTS users;'
users_table = """
CREATE TABLE users (
  username varchar(50) NOT NULL,
  email varchar(50),
  PRIMARY KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
data = """
INSERT INTO sule.users (username, email) 
VALUES 
    ('Sule1', 'sule1@example.com'),
    ('Sule2', 'sule2@example.com'),
    ('Sule3', 'sule3@example.com'),
    ('Sule4', 'sule4@example.com'),
    ('Sule5', 'sule5@example.com');
"""

cursor.execute(drop_table)
cursor.execute(users_table)
cursor.execute(data)

# Function to find emails
def find_emails(keyword):
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [('Not found.', 'Not Found.')]
    return user_emails

# Function to insert new email
def insert_email(name, email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    response = ''
    if len(name) == 0 or len(email) == 0:
        response = 'Username or email can not be empty!!'
    elif not any(result):
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{email}');
        """
        cursor.execute(insert)
        response = f'User {name} and {email} have been added successfully'
    else:
        response = f'User {name} already exists.'
    return response

# Route to search emails
@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_name = request.form['user_keyword']
        user_emails = find_emails(user_name)
        return render_template('emails.html', name_emails=user_emails, keyword=user_name, show_result=True)
    else:
        return render_template('emails.html', show_result=False)

# Route to add new email
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['useremail']
        result = insert_email(user_name, user_email)
        return render_template('add-email.html', result_html=result, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
