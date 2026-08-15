**Version 1 → Python list storage**
**Version 2 → MySQL database storage**

### Student Management System History

**1. Initial Version — Python List**

* Student records stored temporarily in a Python list.
* Data disappears when the program terminates.
* CRUD operations performed on Python data structures.

**2. Why Database?**

* Python list is temporary storage.
* Data should persist after the program closes.
* Database provides permanent/persistent storage.
* MySQL allows structured querying and reliable data management.

**3. Database Integration — Day-by-Day Learning**

* Day 1: Understanding database vs Python list
* Day 2: MySQL connection
* Day 3: Connection vs cursor
* Day 4: SQL queries and `execute()`
* Day 5: `commit()` and `rollback()`
* Day 6: `fetchone()` and `fetchall()`
* Day 7: CRUD operations with MySQL
* Day 8: Exception handling, validation, `rowcount`, and completing the application

**4. Before Database Workflow**

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

**5. Current Database Workflow**

```text
User
 ↓
Python Program
 ↓
MySQL Connector
 ↓
Connection
 ↓
Cursor
 ↓
SQL Query
 ↓
MySQL Database
 ↓
Result / Modification
 ↓
fetch / commit / rollback
```

**6. Current Features**

* Register student
* View students
* Search student
* Update student
* Delete student
* Add marks
* Calculate grade
* Student statistics
* Input validation
* MySQL persistence
* Exception handling

The current code already demonstrates this progression clearly. 


