import re
user=[]
d={}
while True:
    print("Welcome to the User Register System")
    c=int(input("1.Register\n2.Login\n3.Forget"))
    if c==1:
        F_name=input("Enter Your First Name:")#more than one letter
        L_name=input("Enter Your Last Name:")
        Email=input("Enter Your Email:")
        if re.match(r"^[a-z]+[0-9]*@gmail.com$",Email):
            Password=input("Enter a Password of length 8 and begin with capital letter,small letter,symbols and numbers(ex:Darshu@123):")
            if re.match(r"^[A-Z]+[a-z]+[!@$%*&#]+[0-9]+$",Password) and len(Password)>=8:
                if Email in user:
                    print("User already exist,please login.")
                else:
                    print("Registration successful.")
                    user.append(Email)
                    print(user)
                    d[Email]=Password
                    print(d)
            else:
                print("Invalid Password,enter a valid password")
        else:
             print("Invalid email,enter a valid Email")
    elif c==2:
        Email=input("Enter Your Email:")
        Password=input("Enter your Password")
        if Email in user:
            if d[Email]==Password:
                print(f"{F_name} logged in successfully.")
            else:
                print("Either Email or Password doesn't match .\nPlease try again.")
        else:
            print("Usernot found!\nPlease Register.")
    elif c==3:#forget password take user email,enter new password and show your password is updated to
        
    else:
        print("--Invalid choice exiting the program--")
        break

            
        
        
    