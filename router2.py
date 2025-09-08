IMPORT Flask, request, jsonify FROM flask
IMPORT sqlite3

INITIALIZE app AS Flask

FUNCTION get_db_connection:
    CREATE connection TO 'users.db' SQLite database
    SET row factory to sqlite3.Row FOR connection
    RETURN connection

FUNCTION login:
    SET username TO value FROM request's form with key 'username'
    SET password TO value FROM request's form with key 'password'

    # Construct vulnerable SQL query
    SET query TO "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    SET conn TO get_db_connection()
    SET user TO result OF executing query ON conn
    CLOSE conn

    IF user EXISTS:
        RETURN JSON response WITH message "Login successful!"
    ELSE:
        RETURN JSON response WITH message "Login failed!" AND HTTP status 401

# Main execution block
IF this script is the main module:
    RUN app IN debug mode
