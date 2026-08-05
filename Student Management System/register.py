import re
print("========== Student Management System ==========\n1. Register Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Add Marks\n7. Calculate Grade\n8. Student Statistics\n9. Exit")
students=[]
def register_student(roll_Number,name,age,email,course,marks,grade):
    students.append({
        "roll_number": roll_Number,
        "name": name,
        "age": age,
        "email": email,
        "course": course,
        "marks": marks,
        "grade": grade
    })
    
def view_students():
    print( f"Roll\t\tName\tCourse\tMarks\tGrade\t")
    print("-------------------------------------")
    for student in students:
        print(f"{student['roll_number']}\t{student['name']}\t{student['course']}\t{student['marks']}\t{student['grade']}")
    
def search_student(roll_number):
    for student in students:
        if student["roll_number"] == roll_number:
            print(f"{roll_number} found in the list")
            return f"Roll Number: {student['roll_number']}\nName: {student['name']}\nAge: {student['age']}\nEmail: {student['email']}\nCourse: {student['course']}\nMarks: {student['marks']}\nGrade: {student['grade']}"
    print(f"{roll_number} not in the list")
    return None
    
def update_student(roll_number):
    if search_student(roll_number):
        for student in students:
            if student["roll_number"]==roll_number:         
                c=int(input("1.Update Name\n2.Update Age\n3Update Email\n4Update Course\nEnter a choice:"))
                
                if c==1:
                    name=input("Enter a name:")
                    student["name"]=name
                elif c==2:
                    age=int(input("Enter a age:"))
                    if age>18:
                        student["age"]=age
                    else:
                        print("Age should be greater than 18")
                elif c==3:
                    email=input("Enter a email:")
                    student["email"]=email
                elif c==4:
                    course=input("Enter a course:")
                    student["course"]=course
                else:
                    print("Invalid choice")
                    break
    
def delete_student():
    roll_number=str(input("enter a roll number u want to delete:"))
    c=input("are u sure (y/n)?:")
    if c=="y":
        for student in students:
            if student["roll_number"]==roll_number:
                students.remove(student)
                return "remove successfully"
            else:
                return "roll number not found"
        
def add_marks(roll_number):
    marks=int(input("enter marks:"))
    while True:
        if 0<=marks<=100:
            for student in students:
                if student["roll_number"]==roll_number:
                    student["marks"]=marks
            return f"Marks added successfully"
        else:
            marks=int(input("Invalid marks. Please enter a value between 0 and 100."))


def calculate_grade(roll_number):
    for student in students:
        if student["roll_number"]==roll_number:
            if 90<=student["marks"]<=100:
                student["grade"]="A+"
                return "Grade A+"
            elif 80<=student["marks"]<=89:
                student["grade"]="A"
                return "Grade A"
            elif 70<=student["marks"]<=79:
                student["grade"]="B"
                return "Grade B"
            elif 60<=student["marks"]<=69:
                student["grade"]="C"
                return "Grade C"
            elif 50<=student["marks"]<=59:
                student["grade"]="D"
                return "Grade D"
            elif student["marks"]<50:
                student["grade"]="Fail"
                return "Fail"
        else:
            return "Roll number not found"
def student_statistics():
    if len(students)==0:
        print("No students registered yet.")
        return
    avg=0
    print(f"Total students={len(students)}")
    for student in students:
        avg+=student["marks"]
    print(f"Average marks={avg/len(students)}")          
    pas=0
    fail=0
    min=float('inf')
    max=float('-inf')   
    topper=''     
    for student in students:
        if student["marks"]>50:
            pas+=1
        else:
            fail+=1
        if student["marks"]>max:
            max=student["marks"]
            topper=student["name"]
        if student["marks"]<min:
            min=student["marks"]
    
    print(f"Highest marks={max}") 
    print(f"Lowest marks={min}")           
    print(f"Passed students:{pas}")
    print(f"Failed students:{fail}")
    print(f"Topper Name:{topper}")
        

def main():
    while True:
        c=int(input("\nEnter a choice: "))
        if c==1:
            roll_Number = str(input("Enter Roll Number: "))
            while not re.match(r"^1GG[0-9]{2}[A-Z]{2}[0-9]{3}$", str(roll_Number)):
                print("Invalid roll number format. Please enter a valid roll number.")
                roll_Number = str(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            while age<18:
                    print("Age should be greater than 18.")
                    age = int(input("Enter Age: "))
            else:
                email = input("Enter Email: ")
                while not re.match(r"^[a-z]+[0-9]*@gmail.com$", email):
                    print("Invalid email format. Please enter a valid Gmail address.")
                    email = input("Enter Email: ")
                course = input("Enter Course: ")
                marks=""
                grade=""
                register_student(roll_Number,name,age,email,course,marks,grade)
        elif c==2:
            view_students()
        elif c==3:
            roll_number=str(input("Enter a roll number:"))
            print(search_student(roll_number))
        elif c==4:
            roll_num=str(input("Enter a roll number:"))
            update_student(roll_num)
        elif c==5:
            delete_student()
        elif c==6:
            roll_num=str(input("Enter a roll number:"))
            print(add_marks(roll_num))
        elif c==7:
            roll_num=str(input("Enter a roll number:"))
            print(calculate_grade(roll_num))
        elif c==8:
            student_statistics()
        elif c==9:
            break
main()