# 69_python_database_sqlite.py
# SQLite Database - 10 practical programs/features
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")
cur.executemany("INSERT INTO students(name, marks) VALUES (?, ?)",
                [("Prashant", 85), ("Aman", 72), ("Riya", 91)])

cur.execute("SELECT * FROM students")
print("1. All students:", cur.fetchall())

cur.execute("SELECT name, marks FROM students WHERE marks >= 80")
print("2. Marks >= 80:", cur.fetchall())

cur.execute("UPDATE students SET marks = ? WHERE name = ?", (88, "Prashant"))
print("3. Updated records:", cur.rowcount)

cur.execute("DELETE FROM students WHERE name = ?", ("Aman",))
print("4. Deleted records:", cur.rowcount)

cur.execute("SELECT COUNT(*) FROM students")
print("5. Student count:", cur.fetchone()[0])

cur.execute("SELECT AVG(marks) FROM students")
print("6. Average marks:", round(cur.fetchone()[0], 2))

cur.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1")
print("7. Top student:", cur.fetchone())

cur.execute("SELECT * FROM students WHERE name = ?", ("Riya",))
print("8. Search by name:", cur.fetchone())

cur.execute("SELECT name FROM students ORDER BY name")
print("9. Sorted names:", [row[0] for row in cur.fetchall()])

conn.commit()
cur.execute("SELECT * FROM students")
print("10. Final table:", cur.fetchall())
conn.close()
