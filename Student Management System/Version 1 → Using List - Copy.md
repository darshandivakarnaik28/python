# Problem Statement

Create a **Student Management System** for a training institute.

The system should allow the user to register students, view students, search students, update student information, delete students, calculate grades, and display statistics.

The application should continue running until the user chooses Exit.

---

# Concepts Covered

✅ Variables

✅ Input / Output

✅ Data Types

✅ Operators

✅ Conditional Statements

✅ Loops

✅ Nested Loops

✅ Lists

✅ Dictionaries (Optional if covered)

✅ String Functions

✅ List Methods

✅ Functions

✅ Return Statement

✅ Parameters & Arguments

✅ Membership Operators (`in`, `not in`)

✅ Identity Operators (`is`, `is not`)

✅ Logical Operators

✅ Break / Continue

---
# Menu

```
========== Student Management System ==========
1. Register Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Add Marks
7. Calculate Grade
8. Student Statistics
9. Exit
===============================================
```

---

# Student Details

Each student should have

```
Roll Number
Name
Age
Email
Course
Marks
Grade
```

Store them in a list.

Example

```python
students = [
    ["101","Rahul",21,"rahul@gmail.com","Python",89,"A"],
    ...
]
```

---

# Feature 1

## Register Student

Take

* Roll Number
* Name
* Age
* Email
* Course

Conditions

* Roll Number should be unique.
* Age must be greater than 16.
* Email must contain "@"
* Name cannot be empty.

Store the student.

---

# Feature 2

## View Students

Display

```
Roll    Name     Course      Marks    Grade
----------------------------------------------
101     Rahul    Python       89        A
102     Kiran    Java         76        B
```

If no students

```
No Students Found
```

---

# Feature 3

## Search Student

Search using Roll Number.

If found

Display all details.

Otherwise

```
Student Not Found
```

---

# Feature 4

## Update Student

Search using Roll Number.

Allow updating

```
Name
Age
Email
Course
```

---

# Feature 5

## Delete Student

Ask Roll Number.

Delete the student.

Ask

```
Are you sure?

Y/N
```

---

# Feature 6

## Add Marks

Search Student

Take marks

```
0-100
```

Validate input.

Store marks.

---

# Feature 7

## Calculate Grade

```
90-100   A+

80-89    A

70-79    B

60-69    C

50-59    D

Below 50 Fail
```

Store grade.

---

# Feature 8

## Statistics

Display

```
Total Students

Average Marks

Highest Marks

Lowest Marks

Passed Students

Failed Students

Topper Name
```

---

# Feature 9

## Exit

Ask confirmation.

---

# Required Functions

Students **must** create separate functions.

```
register_student()

view_students()

search_student()

update_student()

delete_student()

add_marks()

calculate_grade()

statistics()

menu()

main()
```

---

# Validation Rules

```
Roll Number cannot be duplicate

Age > 16

Marks between 0-100

Email contains @

Name cannot be empty
```

---

# Bonus Challenges (For Fast Learners)

### Level 1

Sort students by

* Name
* Marks
* Roll Number

---

### Level 2

Search student by partial name.

Example

```
Enter Name:

ra
```

Output

```
Rahul

Pranav

Rajesh
```

---

### Level 3

Find Top 3 Students.

---

### Level 4

Display Grade Report

```
A+ : 4 Students

A  : 8 Students

B  : 6 Students

C  : 3 Students

Fail : 2 Students
```

---

### Level 5

Generate Student ID

```
EXS001

EXS002

EXS003
```

Automatically.


