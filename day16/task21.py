import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS std (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
''')

# Insert data using placeholders and correct data types
cursor.execute("INSERT INTO std (name, age, grade) VALUES (?, ?, ?)", ("Prathap", 25, "A"))
cursor.execute("INSERT INTO std (name, age, grade) VALUES (?, ?, ?)", ("Ibrahim", 26, "B"))
cursor.execute("INSERT INTO std (name, age, grade) VALUES (?, ?, ?)", ("Kiran", 27, "C"))

# Select all data and print it
cursor.execute("SELECT * FROM std")
all_students = cursor.fetchall()
print("All students:", all_students)
print()

# Select names of students older than 26
cursor.execute("SELECT name, age FROM std WHERE age > ?", (26,))
older_students = cursor.fetchall()
print("Students older than 26:")
for row in older_students:
    print(row)
print()

# Update Kiran's age
cursor.execute("UPDATE std SET age = ? WHERE name = ?", (25, "Kiran"))

# Delete Ibrahim
cursor.execute("DELETE FROM std WHERE name = ?", ("Ibrahim",))

# Select all data after update and delete
cursor.execute("SELECT * FROM std")
updated_students = cursor.fetchall()
print("\nStudents after update and delete:", updated_students)

conn.commit()
conn.close()