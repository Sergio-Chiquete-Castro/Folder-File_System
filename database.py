import mysql.connector

def setup_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="******"
    )

    mycursor = db.cursor()
    mycursor.execute('CREATE DATABASE IF NOT EXISTS mydatabase')
    db.database = 'mydatabase'

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_name VARCHAR(255) NOT NULL,
        tag VARCHAR(255) NOT NULL
    )
    ''')

    mycursor.close()
    db.close()

def add_file_and_tag(file_name, tag):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="******"
        database="mydatabase"
    )

    mycursor = db.cursor()

    sql = "INSERT INTO files (file_name, tag) VALUES (%s, %s)"
    val = (file_name, tag)
    mycursor.execute(sql, val)

    db.commit()

    mycursor.close()
    db.close()

def fetch_tags(file_name):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="******"
        database="mydatabase"
    )

    mycursor = db.cursor()

    sql = "SELECT tag FROM files WHERE file_name = %s"
    val = (file_name,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    print(f"Tags for {file_name}:")
    for row in result:
        print(row[0])

    mycursor.close()
    db.close()

if __name__ == "__main__":
    setup_database()

    while True:
        print("\nMenu:")
        print("1. Add file and tag")
        print("2. Check tags")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = input("Enter the file name: ")
            tag = input("Enter the tag: ")

            with open(file_name, 'w') as file:
                file.write("")
                print(f"Confirmed Creation of {file_name}")

            add_file_and_tag(file_name, tag)

        elif choice == "2":
            file_name = input("Enter the file name: ")

            fetch_tags(file_name)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")
