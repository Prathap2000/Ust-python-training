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
datastd=[("Prathap", 25, "A"),("Ibrahim", 26, "B"),("Kiran", 27, "C")]
cursor.execute("INSERT INTO std (name, age, grade) VALUES (?, ?, ?)", datastd)

cursor.execute("SELECT * FROM std")
all_students = cursor.fetchall()
print("All students:", all_students)
print()

cursor.execute("SELECT name, age FROM std WHERE age > ?", (26,))
older_students = cursor.fetchall()
print("Students older than 26:")
for row in older_students:
    print(row)
print()
cursor.execute("UPDATE std SET age = ? WHERE name = ?", (25, "Kiran"))
cursor.execute("DELETE FROM std WHERE name = ?", ("Ibrahim",))

cursor.execute("SELECT * FROM std")
updated_students = cursor.fetchall()
print("\nStudents after update and delete:", updated_students)
conn.commit()
conn.close()