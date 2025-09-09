from flask import Flask, jsonify
import sqlite3
import foo
import bar

app = Flask(__name__)

# Connect to the SQLite database (or create it)
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = bar.form['username']
    password = bar.form['password']

    str = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    foo = init_foo()
    user = foo.execute(str).fetchone()
    foo.close()

    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
