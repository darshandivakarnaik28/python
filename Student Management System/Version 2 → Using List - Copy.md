# Student Management System — Learning Journey

## Day 1 — Understanding the Need for a Database

### Before using MySQL

Initially, the student records were stored in a Python list.

```python
students = []
```

The basic flow was:

```text
User
 ↓
Python Program
 ↓
Python List
 ↓
CRUD Operations
 ↓
Program Ends
 ↓
Data Lost
```

### Problem

The Python list stores data only while the program is running.

If the program is closed:

```text
Program running → Data exists
Program closed   → Data disappears
```

### Why move to a database?

I wanted the student records to be **persistent**, so I decided to use MySQL.

The new idea was:

```text
Python Program
      ↓
    MySQL
      ↓
Permanent data storage
```

---

# Day 2 — Understanding MySQL Connection

First, I learned how Python communicates with MySQL.

I used:

```python
import mysql.connector
```

Then I created a connection:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="studentdb"
)
```

### What I learned

* `mysql.connector` is the Python module used to connect to MySQL.
* `connect()` establishes the connection between Python and MySQL.
* `connection` stores the returned connection object.
* `host`, `user`, `password`, and `database` are parameters supplied to `connect()`.

### Connection flow

```text
Python Program
      ↓
mysql.connector
      ↓
connect()
      ↓
MySQL Database
```

---

# Day 3 — Connection vs Cursor

After establishing the connection, I learned that the connection itself does not execute SQL queries.

I created a cursor:

```python
cursor = connection.cursor()
```

### What is a cursor?

The cursor is used to **execute SQL statements** and retrieve their results.

So:

```text
connection
    ↓
creates cursor
    ↓
cursor.execute()
    ↓
SQL query
```

I also learned the difference:

```text
Connection → communication with database
Cursor     → execution of SQL queries
```

---

# Day 4 — Creating the Database Table

I created the `students` table in MySQL with columns such as:

```text
roll_number
name
age
email
course
marks
grade
```

I learned that the `roll_number` can be used as the **PRIMARY KEY**.

### Why primary key?

Because the roll number should be unique.

```text
101 → Rahul
102 → Kiran
103 → Arjun
```

Two students should not have the same primary key.

---

# Day 5 — INSERT and Parameterized Queries

I learned how to insert a student into MySQL.

```sql
INSERT INTO students
(
    roll_number,
    name,
    age,
    email,
    course
)
VALUES
(%s,%s,%s,%s,%s)
```

Then I created a Python tuple:

```python
values = (roll_number, name, age, email, course)
```

and executed:

```python
cursor.execute(sql, values)
```

### Why not directly put user input into SQL?

I learned about **parameterized queries** and SQL injection.

Instead of constructing SQL with user input directly, I use:

```python
cursor.execute(sql, values)
```

This separates:

```text
SQL statement
     +
User data
```

---

# Day 6 — `commit()` and `rollback()`

This was an important concept.

After `INSERT`, the operation is not considered permanently completed until the transaction is committed.

```python
connection.commit()
```

### Successful transaction

```text
INSERT
 ↓
execute()
 ↓
commit()
 ↓
Data permanently stored
```

### Failed transaction

```text
execute()
 ↓
Exception
 ↓
rollback()
 ↓
Undo transaction
```

I learned:

```text
INSERT → commit()
UPDATE → commit()
DELETE → commit()

SELECT → no commit()
```

---

# Day 7 — Reading Data: `SELECT`

I learned how to retrieve records.

```sql
SELECT * FROM students
```

Then:

```python
cursor.execute(sql)
```

To retrieve all records:

```python
rows = cursor.fetchall()
```

### `fetchall()`

It returns all rows.

For example:

```python
[
    (101, "Rahul", ...),
    (102, "Kiran", ...),
    (103, "Arjun", ...)
]
```

I learned that:

```text
rows → collection of rows
row  → one row
```

So:

```python
for row in rows:
    ...
```

processes each student one by one.

---

# Day 8 — Understanding Tuples and Indexing

I learned that MySQL Connector returns a row as a tuple by default.

For example:

```python
row = (101, "Rahul", 20, "rahul@gmail.com", "CSE", 85, "A")
```

The indexes are:

```text
row[0] → roll_number
row[1] → name
row[2] → age
row[3] → email
row[4] → course
row[5] → marks
row[6] → grade
```

I learned that `row[1]` is **indexing**, not calling the `index()` method.

---

# Day 9 — `fetchone()` and Searching

For searching one student by roll number, I used:

```sql
SELECT * FROM students
WHERE roll_number = %s
```

Because `roll_number` is the primary key, the search can return:

```text
One student
OR
No student
```

Therefore I use:

```python
row = cursor.fetchone()
```

If no student exists:

```python
row is None
```

So:

```python
if row is None:
    print("Student not found")
else:
    display(row)
```

I learned the difference:

```text
fetchall() → multiple rows
fetchone() → one row
```

---

# Day 10 — UPDATE and `rowcount`

Then I learned how to update an existing student.

Example:

```sql
UPDATE students
SET marks = %s
WHERE roll_number = %s
```

The `WHERE` clause is important because it identifies **which student's record should be modified**.

I learned about:

```python
cursor.rowcount
```

It tells us how many rows were affected.

For example:

```text
rowcount = 1
→ student found and affected

rowcount = 0
→ no matching student
```

So we don't simply assume the update succeeded.

---

# Day 11 — DELETE

I learned how to delete a student:

```sql
DELETE FROM students
WHERE roll_number = %s
```

Again, the `WHERE` condition ensures that we delete the **intended student**, rather than every student.

The flow became:

```text
DELETE
 ↓
execute()
 ↓
rowcount
 ↓
0 → Student not found
1 → commit()
      ↓
   Delete successful
```

---

# Day 12 — Exception Handling

I learned how to handle MySQL errors:

```python
try:
    cursor.execute(sql, values)
    connection.commit()

except mysql.connector.Error as err:
    connection.rollback()
    print(err)
```

I also learned how MySQL error numbers can identify particular errors.

For example, duplicate primary-key insertion can produce:

```python
err.errno == 1062
```

Then I can give a meaningful message such as:

```text
Roll number already exists
```

instead of displaying only a generic error.

---

# Day 13 — Input Validation

I added validation before inserting data.

For example, roll-number validation:

```python
re.match(
    r"^1GG[0-9]{2}[A-Z]{2}[0-9]{3}$",
    roll_number
)
```

Email validation:

```python
re.match(
    r"^[a-z]+[0-9]*@gmail.com$",
    email
)
```

I also validated age and marks.

The important lesson was:

```text
User Input
    ↓
Validation
    ↓
Valid?
 ┌──┴──┐
Yes    No
 ↓      ↓
SQL    Error message
```

---

# Day 14 — Connecting Everything Together

Finally, I connected all the operations into one menu-driven application.

```text
1. Register Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Add Marks
7. Calculate Grade
8. Student Statistics
9. Exit
```

I learned to establish the connection **once**:

```python
connection = mysql.connector.connect(...)
cursor = connection.cursor()
```

Then reuse the same connection and cursor inside the menu loop.

```text
Program starts
      ↓
Connection established
      ↓
Cursor created
      ↓
       ┌──────────────┐
       │  Menu Loop   │
       └──────┬───────┘
              ↓
       CRUD operations
              ↓
       More menu operations
              ↓
            Exit
              ↓
       Close resources
```

This avoids repeatedly opening a new database connection for every menu operation.

---

# 🎯 Final Learning Flow

This is the complete journey I followed:

```text
Python List
    ↓
Problem with temporary storage
    ↓
Why Database?
    ↓
MySQL
    ↓
mysql.connector
    ↓
Connection
    ↓
Cursor
    ↓
SQL
    ↓
INSERT
    ↓
Parameterized Queries
    ↓
commit()
    ↓
rollback()
    ↓
SELECT
    ↓
fetchone()
    ↓
fetchall()
    ↓
Tuples & Indexing
    ↓
UPDATE
    ↓
rowcount
    ↓
DELETE
    ↓
Exception Handling
    ↓
Input Validation
    ↓
CRUD
    ↓
Menu-driven application
    ↓
Complete Student Management System
```




