Method	Purpose
fetchone()	Retrieves one row
fetchall()	Retrieves all remaining rows

There is also fetchmany(n) when you want a specific number of rows.

Absolutely. 👍 We'll stop here and continue from **this exact point tomorrow**.

# 📘 Today's Learning Report

**Topic:** Python + MySQL Integration — Database CRUD Architecture
**Session:** Continuation

### 1. Database as the Source of Truth

You understood that `students = []` only stores data temporarily in RAM.

We changed the architecture to:

```text
Python Application
       ↓
MySQL Connector
       ↓
MySQL Database
       ↓
students table
```

MySQL becomes the **persistent source of student records**.

---

### 2. Connection Lifecycle

You learned the correct architecture:

```text
Program starts
      ↓
Establish ONE connection
      ↓
Create cursor
      ↓
Menu loop
      ↓
Register / View / Search / Update / Delete
      ↓
Exit
      ↓
Close cursor
      ↓
Close connection
```

You correctly understood that the connection should **not** be created inside the `while` loop.

---

### 3. Connection Failure Handling

You learned that if MySQL connection fails:

```text
Connection failed
      ↓
Show meaningful error
      ↓
Stop application
```

Because the main database operations cannot work without a connection.

---

### 4. Cursor Passing

You learned why we prefer:

```text
register_student(cursor)
```

instead of using a global cursor.

Advantages:

* Easier to read
* Easier to test
* Function explicitly receives its database dependency
* Avoids hidden global state

---

### 5. Parameterized SQL

You learned that student data should be passed separately from the SQL statement.

Conceptually:

```text
SQL query
    +
Python values
    ↓
cursor.execute()
```

This is important for:

* **SQL injection prevention**
* Correct handling of user data
* Proper separation of SQL instructions and data

---

### 6. INSERT Operation

You learned the complete conceptual flow:

```text
Student details
      ↓
Parameterized INSERT
      ↓
cursor.execute()
      ↓
MySQL
      ↓
commit()
      ↓
Permanent record
```

If the operation fails:

```text
Exception
    ↓
rollback()
```

---

### 7. Primary Key Handling

You correctly understood:

* `roll_number` is the primary key.
* It must be unique.
* A normal `INSERT` cannot create another row with the same roll number.
* Python should catch the database exception and show a meaningful message such as **"Roll number already exists."**

---

### 8. Today's Final Concept

We discussed **positional parameter matching**.

You correctly answered that if the values are supplied in the wrong order:

```text
email → marks
marks → course
course → email
```

the values won't automatically be rearranged.

You also correctly identified that **data types and validation can become incorrect**.

---

# ⭐ Today's Performance

**Score: 9.7/10**

### Strong points today:

* Database architecture ✅
* Connection lifecycle ✅
* Exception handling reasoning ✅
* Dependency passing ✅
* Parameterized queries ✅
* Primary-key reasoning ✅
* CRUD architecture ✅

### Tomorrow's starting point:

We'll start exactly here:

> **How the values tuple is matched to the `%s` placeholders → execute the INSERT → commit → handle duplicate roll numbers → verify the record in MySQL.**

Then we'll move quickly into **View, Search, Update, and Delete**.

Good session today. 👍 **Tomorrow we start the actual `Register Student → MySQL` implementation.**
