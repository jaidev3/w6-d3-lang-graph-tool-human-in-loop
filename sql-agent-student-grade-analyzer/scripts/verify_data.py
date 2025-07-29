import sqlite3

# Connect to the database
conn = sqlite3.connect('grades.db')
cursor = conn.cursor()

print("=== Database Verification ===\n")

# 1. Show all students and their grades
print("1. All students and their grades (first 10 records):")
cursor.execute('SELECT * FROM students LIMIT 10')
for row in cursor.fetchall():
    print(f"  {row[1]} - {row[2]}: {row[3]}")

# 2. Average grade by subject
print("\n2. Average grade by subject:")
cursor.execute('''
SELECT subject, AVG(grade) as avg_grade, COUNT(*) as num_students
FROM students 
GROUP BY subject
ORDER BY avg_grade DESC
''')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:.1f} (from {row[2]} students)")

# 3. Top 5 students by average grade
print("\n3. Top 5 students by average grade:")
cursor.execute('''
SELECT name, AVG(grade) as avg_grade, COUNT(*) as subjects_taken
FROM students 
GROUP BY name
ORDER BY avg_grade DESC
LIMIT 5
''')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:.1f} average (took {row[2]} subjects)")

# 4. Grade distribution
print("\n4. Grade distribution:")
cursor.execute('''
SELECT 
    CASE 
        WHEN grade >= 90 THEN 'A (90-100)'
        WHEN grade >= 80 THEN 'B (80-89)'
        WHEN grade >= 70 THEN 'C (70-79)'
        ELSE 'D (Below 70)'
    END as grade_letter,
    COUNT(*) as count
FROM students
GROUP BY grade_letter
ORDER BY count DESC
''')
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} students")

# 5. Students with grades below 80
print("\n5. Students with grades below 80:")
cursor.execute('''
SELECT name, subject, grade
FROM students
WHERE grade < 80
ORDER BY grade ASC
''')
for row in cursor.fetchall():
    print(f"  {row[0]} - {row[1]}: {row[2]}")

# 6. Subject with highest average
print("\n6. Subject with highest average:")
cursor.execute('''
SELECT subject, AVG(grade) as avg_grade
FROM students
GROUP BY subject
ORDER BY avg_grade DESC
LIMIT 1
''')
row = cursor.fetchone()
print(f"  {row[0]}: {row[1]:.1f}")

conn.close()

print("\n=== Verification Complete ===")
print("\nYou can now use the SQL agent to ask questions like:")
print("- 'What is the average grade in Math?'")
print("- 'Who are the top 3 students by average grade?'")
print("- 'How many students have grades below 80?'")
print("- 'What is the grade distribution across all subjects?'")
print("- 'Which subject has the highest average grade?'") 