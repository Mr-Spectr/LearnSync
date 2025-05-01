import sqlite3

def create_database():
    connection = sqlite3.connect("learning_management.db")
    cursor = connection.cursor()

    # Create Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Create Assessments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        topic TEXT,
        score INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    connection.commit()
    connection.close()

def register_user(username, password):
    connection = sqlite3.connect("learning_management.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    connection.commit()
    connection.close()

def take_assessment(user_id, topic, score):
    connection = sqlite3.connect("learning_management.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO assessments (user_id, topic, score) VALUES (?, ?, ?)", (user_id, topic, score))

    connection.commit()
    connection.close()

def main():
    create_database()

    print("Welcome to the Learning Management Assessment System!")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # For simplicity, we assume a successful login
    register_user(username, password)
    user_id = 1  # Assume the user has ID 1 for simplicity

    topic = input("Enter the assessment topic: ")
    score = int(input("Enter your score: "))

    take_assessment(user_id, topic, score)

    print("\nAssessment recorded successfully!")

if __name__ == "__main__":
    main()

