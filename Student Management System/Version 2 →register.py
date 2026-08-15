import re
import mysql.connector
print("========== Student Management System ==========\n1. Register Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Add Marks\n7. Calculate Grade\n8. Student Statistics\n9. Exit")
def roll_validation(roll_number):
    if re.match(r"^1GG[0-9]{2}[A-Z]{2}[0-9]{3}$",roll_number):
        return True
    else:
        return False
def email_validation(email):
    if re.match(r"^[a-z]+[0-9]*@gmail.com$", email):
        return True
    else:
        return False

def register_student(cursor,connection):
    roll_number = str(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age > 18: "))
    email = input("Enter Email: ")
    course = input("Enter Course: ")
    values=(roll_number,name,age,email,course)
    sql="""INSERT INTO students (roll_number,name,age,email,course)
    VALUES(%s,%s,%s,%s,%s)"""    
    if roll_validation(roll_number) ==True and email_validation(email)==True and age >18:
        try:
            cursor.execute(sql,values)
            connection.commit()
            return f"Registration Succesfull"
        except mysql.connector.Error as err:
            if err.errno==1062:
                connection.rollback()
                return f"Roll_number already exists"
            else:
                connection.rollback()
                return f"Database error"
    return f"Enter a valid rollnumber and email_id and age must be grater the 18"
        
def view_students(cursor):
    sql="""SELECT * FROM students"""
    try:
        cursor.execute(sql)
        rows= cursor.fetchall()
        if not rows:
            return "The student table is empty"
        else:
            for row in rows:
                display(row)
    except mysql.connector.Error as err:
        print("Database error :",err)

def display(row):
    print(f"Roll Number:{row[0]}")
    print(f"Name:{row[1]}")
    print(f"Age:{row[2]}")
    print(f"Email:{row[3]}")
    print(f"Course:{row[4]}")
    print(f"Marks:{row[5]}")
    print(f"Grade:{row[6]}\n\n")

def search_student(cursor):
    roll_number=str(input(("Enter roll number of student :")))
    sql="""SELECT * FROM students WHERE roll_number=%s"""    
    values=(roll_number,)
    try:
        cursor.execute(sql,values)
        row=cursor.fetchone()
        if row is None:
            print("Student not found")
        else:
            print("Student Found")
            display(row)
    except mysql.connector.Error as err:
        print("Database error:",err)

def update_student(cursor,connection):
    roll_number=str(input("Enter a roll_number to be update :"))
    c=int(input("1.Update Name\n2.Update Age\n3Update Email\n4Update Course\nEnter a choice:"))
    
    if c==1:
        name=input("Enter a name:")
        sql="""UPDATE students SET name=%s WHERE roll_number=%s"""
        values=(name,roll_number)
        try:
            cursor.execute(sql,values)
            connection.commit()
            if cursor.rowcount>=1:
                return "Update successfully"
            else:
                return "Roll number not found"
        except mysql.connector.Error as err:
            connection.rollback()
            return f"Database error:{err}"
    elif c==2:
        age=int(input("Enter a age:"))
        if age>18:                        
            sql="""UPDATE students SET age=%s WHERE roll_number=%s"""
            values=(age,roll_number)
            try:
                cursor.execute(sql,values)
                connection.commit()
                if cursor.rowcount>=1:
                    return f"Age updated successfully"
                else:
                    return "Roll number not found"
            except mysql.connector.Error as err:
                connection.rollback()
                return f"Database error:{err}"
        else:
            return "Age must be greater than 18"

    elif c==3:
        email=input("Enter a email:")
        sql="""UPDATE students SET email=%s WHERE roll_number=%s"""
        values=(email,roll_number)
        try:
            cursor.execute(sql,values)
            connection.commit()
            if cursor.rowcount>=1:
                return f"Email updated successfully"
            else:
                return "Roll number not found"
        except mysql.connector.Error as err:
            cursor.rollback()
            return f"Database error:{err}"
    elif c==4:
        course=input("Enter a course:")
        sql="""UPDATE students SET course=%s WHERE roll_number=%s"""
        values=(course,roll_number)        
        try:
            cursor.execute(sql,values)
            connection.commit()
            if cursor.rowcount>=1:
                return f"course updated successfully"
            else:
                return "Roll number not found"
        except mysql.connector.Error as err:
            cursor.rollback()
            return f"Database error:{err}"
    else:
       return "Invalid choice"
                
    
def delete_student(cursor,connection):
    roll_number=str(input("enter a roll number u want to delete:"))
    c=input("are u sure (y/n)?:")
    if c=="y":
        sql="""DELETE FROM students WHERE roll_number=%s"""
        values=(roll_number,)
        try:
            cursor.execute(sql,values)
            connection.commit()
            if cursor.rowcount>=1:
                return "Delete successfully"
            else:
                return "roll number not found"
        except mysql.connector.Error as err:
            connection.rollback()
            return f"Database error :{err}"
        
def add_marks(cursor,connection):
    marks=int(input("enter marks:"))
    roll_number=str(input("Enter a roll_number: "))
    if 0<=marks<=100:
        sql="""UPDATE students SET marks=%s WHERE roll_number=%s"""
        values=(marks,roll_number)
        try:
            cursor.execute(sql,values)
            connection.commit()
            if cursor.rowcount>=1:
                return f"Marks added successfully"
            else:
                return "Roll_number not found"
        except mysql.connector.Error as err:
                connection.rollback()
                return "Database error :{err}"
    else:
        return "marks shoulbe between of 0 to 100"

def calculate_grade(cursor,connection):
    roll_number=str(input("Enter a roll_number: "))
    sql="""SELECT * FROM students"""
    try:
        cursor.execute(sql)
        student1=cursor.fetchall()
        for student in student1:
            if student[0]==roll_number:
                if 90<=student[5]<=100:
                    grade="A+"
                    
                elif 80<=student[5]<=89:
                    grade= "A"
                    
                elif 70<=student[5]<=79:
                    grade="B"
                    
                elif 60<=student[5]<=69:
                    grade="C"
                    
                elif 50<=student[5]<=59:
                    grade="D"
                    
                elif student[5]<50:
                    grade="Fail"
                    
                sql="""UPDATE students SET grade=%s WHERE roll_number=%s"""
                value=(grade,roll_number)
                try:
                    cursor.execute(sql,value)
                    connection.commit()
                    if cursor.rowcount>=1:
                        return "Grade calculate successfully"
                    else:
                        return "Grade not calculated"
                except mysql.connector.Error as err:
                    return f"Error {err}"
    except mysql.connector.Error as err:
        return f"Error: {err}"
        
def student_statistics(cursor):
    sql="""SELECT COUNT(roll_number) FROM students"""
    try:
        cursor.execute(sql)
        total=cursor.fetchone()
        print (f"Total students ={total[0]}")
    except mysql.connector.Error as err:
        print(f"Error :{err}")
    sql="""SELECT AVG(marks) FROM students"""
    try:
        cursor.execute(sql)
        avg=cursor.fetchone()
        print(f"Average mark={avg[0]}")   
    except mysql.connector.Error as err:
            print(f"Error :{err}")       
    sql="""SELECT COUNT(roll_number) FROM students WHERE marks >= 50"""    
    try:
        cursor.execute(sql)
        studentss=cursor.fetchone()
        print(f"Passed students are:{studentss[0]}")
    except mysql.connector.Error as err:
                print(f"Error :{err}")  
    sql="""SELECT COUNT(roll_number) FROM students WHERE marks<50"""
    try:
        cursor.execute(sql)
        studentss=cursor.fetchone()
        print(f"Failed students are:{studentss[0]}")
    except mysql.connector.Error as err:
        print(f"Error :{err}")  
    sql="""SELECT name,marks FROM students ORDER BY marks DESC LIMIT 1"""
    try:
        cursor.execute(sql)
        studentss=cursor.fetchone()
        print(f"Max score is :{studentss[1]}  {(studentss[0])}")
    except mysql.connector.Error as err:
        print(f"Error :{err}")  
    sql="""SELECT name,marks FROM students ORDER BY marks ASC LIMIT 1"""
    try:
        cursor.execute(sql)
        studentss=cursor.fetchone()
        print(f"Minimum score is :{studentss[1]}  {(studentss[0])} ")
    except mysql.connector.Error as err:
        print(f"Error :{err}")          

def main():
    connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="252800",
    database="studentdb"
    )
    cursor=connection.cursor()
    while True:
        c=int(input("\nEnter a choice: "))
        if c==1:
            print(register_student(cursor,connection))
        elif c==2:
            view_students(cursor)
        elif c==3:
            search_student(cursor)
        elif c==4:
            print(update_student(cursor,connection))
        elif c==5:
            print(delete_student(cursor,connection))
        elif c==6:
            print(add_marks(cursor,connection))
        elif c==7:
            print(calculate_grade(cursor,connection))
        elif c==8:
            student_statistics(cursor)
        elif c==9:
            break
main()