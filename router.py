from flask import Flask, request, jsonify
import sqlite3
import foo

app = Flask(__name__)

# Connect to the SQLite database (or create it)
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vulnerable SQL query construction
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    foo = init_foo()
    user = foo.execute(query).fetchone()
    foo.close()

    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
