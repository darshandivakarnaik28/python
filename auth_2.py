#This is the authentication system using functions
import re
data={}    
def verification(Email,Password):
    if re.match(r"^[a-z]+[0-9]*@gmail.com$",Email) and re.match(r"^[A-Z]+[a-z]+[@#$%^&*]+[0-9]+$",Password):
        return True
    else:
        return False
        
def register(F_name,L_name,Email,Password):
    if verification(Email,Password)==True:    
        if Email in data:
            return ( f"{Email} already exist Please Login")
        else:
            data[Email]={"F_name":F_name,"L_name":L_name,"Password":Password}
            print(data)
            return f"Registration successfull...!"
    else:
        return "enter valid email or password"
        
def login(email,password):
    if verification(email,password)==True:
        if email in data:        
            if data[email]["Password"]==password:
                return f"Logged in\nWell Come {data[email]['F_name']}"
            else:
                return "Either password or email is incorrect"
        else:
            return "Email not registered please register."
    else:
        return "Invalid email or password"
        
      
def control():
    while True:
        enter=int(input("1.Register\n2.Login\n"))
        if enter==1:
            F_name=input("\nEnter your First name:")
            L_name=input("Enter your Last name:")
            Email=input("Enter your Email:")
            Password=input("Enter password")
            print(register(F_name,L_name,Email,Password))
        elif enter==2:
            Email=input("\nEmail:")
            Password=input("Password:")
            print(login(Email,Password))
            for key,value in data.items():
                for k,v in value.items():
                    print( "\ndetails of all users:\nEmail:",key,"\nFirst Name:",k,"\nLast Name:",v)
                    break
        else:
            print("good bye...!")
            break
                    
            
control()
