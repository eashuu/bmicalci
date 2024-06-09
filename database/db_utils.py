import mysql.connector
import bcrypt
from config.config import DB_CONFIG

def create_connection():
    """Create a database connection."""
    connection = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    return connection

def user_exists(username):
    """Check if a user exists in the database."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count > 0

def add_user(username, password):
    """Add a new user to the database."""
    connection = create_connection()
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    connection.commit()
    cursor.close()
    connection.close()

def get_user_password(username):
    """Retrieve the password for a given username."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return result[0]
    return None

def verify_password(stored_password, provided_password):
    """Verify if the provided password matches the stored password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
