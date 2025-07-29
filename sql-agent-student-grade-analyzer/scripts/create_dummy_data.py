import sqlite3
import random

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('grades.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL
)
''')

# Sample data for students
students_data = [
    # Math grades
    ("Alice Johnson", "Math", 95),
    ("Bob Smith", "Math", 87),
    ("Carol Davis", "Math", 92),
    ("David Wilson", "Math", 78),
    ("Emma Brown", "Math", 89),
    ("Frank Miller", "Math", 83),
    ("Grace Lee", "Math", 96),
    ("Henry Taylor", "Math", 91),
    
    # Science grades
    ("Alice Johnson", "Science", 88),
    ("Bob Smith", "Science", 92),
    ("Carol Davis", "Science", 85),
    ("David Wilson", "Science", 79),
    ("Emma Brown", "Science", 94),
    ("Frank Miller", "Science", 87),
    ("Grace Lee", "Science", 90),
    ("Henry Taylor", "Science", 83),
    
    # English grades
    ("Alice Johnson", "English", 92),
    ("Bob Smith", "English", 85),
    ("Carol Davis", "English", 89),
    ("David Wilson", "English", 76),
    ("Emma Brown", "English", 91),
    ("Frank Miller", "English", 88),
    ("Grace Lee", "English", 94),
    ("Henry Taylor", "English", 82),
    
    # History grades
    ("Alice Johnson", "History", 90),
    ("Bob Smith", "History", 88),
    ("Carol Davis", "History", 87),
    ("David Wilson", "History", 81),
    ("Emma Brown", "History", 93),
    ("Frank Miller", "History", 85),
    ("Grace Lee", "History", 89),
    ("Henry Taylor", "History", 84),
    
    # Additional students for more variety
    ("Ivy Chen", "Math", 94),
    ("Ivy Chen", "Science", 91),
    ("Ivy Chen", "English", 88),
    ("Ivy Chen", "History", 92),
    
    ("Jack Anderson", "Math", 82),
    ("Jack Anderson", "Science", 86),
    ("Jack Anderson", "English", 90),
    ("Jack Anderson", "History", 87),
    
    ("Kate Rodriguez", "Math", 89),
    ("Kate Rodriguez", "Science", 93),
    ("Kate Rodriguez", "English", 85),
    ("Kate Rodriguez", "History", 88),
    
    ("Liam O'Connor", "Math", 91),
    ("Liam O'Connor", "Science", 88),
    ("Liam O'Connor", "English", 92),
    ("Liam O'Connor", "History", 90),
    
    ("Maya Patel", "Math", 86),
    ("Maya Patel", "Science", 89),
    ("Maya Patel", "English", 87),
    ("Maya Patel", "History", 85),
    
    ("Noah Thompson", "Math", 93),
    ("Noah Thompson", "Science", 90),
    ("Noah Thompson", "English", 89),
    ("Noah Thompson", "History", 91),
    
    ("Olivia Garcia", "Math", 88),
    ("Olivia Garcia", "Science", 92),
    ("Olivia Garcia", "English", 94),
    ("Olivia Garcia", "History", 86),
    
    ("Paul Martinez", "Math", 85),
    ("Paul Martinez", "Science", 87),
    ("Paul Martinez", "English", 83),
    ("Paul Martinez", "History", 89),
    
    ("Quinn Williams", "Math", 90),
    ("Quinn Williams", "Science", 94),
    ("Quinn Williams", "English", 91),
    ("Quinn Williams", "History", 88),
    
    ("Rachel Kim", "Math", 87),
    ("Rachel Kim", "Science", 89),
    ("Rachel Kim", "English", 86),
    ("Rachel Kim", "History", 92),
    
    ("Sam Johnson", "Math", 92),
    ("Sam Johnson", "Science", 85),
    ("Sam Johnson", "English", 93),
    ("Sam Johnson", "History", 87),
    
    ("Tina Wang", "Math", 89),
    ("Tina Wang", "Science", 91),
    ("Tina Wang", "English", 88),
    ("Tina Wang", "History", 90),
    
    ("Uma Singh", "Math", 94),
    ("Uma Singh", "Science", 88),
    ("Uma Singh", "English", 92),
    ("Uma Singh", "History", 89),
    
    ("Victor Lopez", "Math", 86),
    ("Victor Lopez", "Science", 90),
    ("Victor Lopez", "English", 85),
    ("Victor Lopez", "History", 93),
    
    ("Wendy Zhang", "Math", 91),
    ("Wendy Zhang", "Science", 87),
    ("Wendy Zhang", "English", 90),
    ("Wendy Zhang", "History", 86),
    
    ("Xavier Rivera", "Math", 88),
    ("Xavier Rivera", "Science", 93),
    ("Xavier Rivera", "English", 87),
    ("Xavier Rivera", "History", 91),
    
    ("Yara Ali", "Math", 93),
    ("Yara Ali", "Science", 89),
    ("Yara Ali", "English", 94),
    ("Yara Ali", "History", 88),
    
    ("Zoe Murphy", "Math", 90),
    ("Zoe Murphy", "Science", 92),
    ("Zoe Murphy", "English", 89),
    ("Zoe Murphy", "History", 85)
]

# Insert the data
cursor.executemany('''
INSERT INTO students (name, subject, grade)
VALUES (?, ?, ?)
''', students_data)

# Commit the changes
conn.commit()

# Verify the data was inserted
cursor.execute('SELECT COUNT(*) FROM students')
total_records = cursor.fetchone()[0]

cursor.execute('SELECT DISTINCT name FROM students')
unique_students = cursor.fetchall()

cursor.execute('SELECT DISTINCT subject FROM students')
subjects = cursor.fetchall()

print(f"Database created successfully!")
print(f"Total records inserted: {total_records}")
print(f"Number of unique students: {len(unique_students)}")
print(f"Subjects: {[subject[0] for subject in subjects]}")

# Show some sample data
print("\nSample data:")
cursor.execute('SELECT * FROM students LIMIT 10')
sample_data = cursor.fetchall()
for row in sample_data:
    print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}, Grade: {row[3]}")

# Close the connection
conn.close()

print("\nDummy data creation completed!") 