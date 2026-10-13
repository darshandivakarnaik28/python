n=int(input("Enter a number: "))
reverse=0
while(n!=0):
    r=n%10
    reverse=(reverse*10)+r
    n=n//10
space=0
while(reverse!=0):
    print("Socker Creation")
    r=reverse%10
    print(space,end=" ")
    space=space*10
    print("* 10 =",space)
    print("Placement of digit")
    print(space,end=" ")
    space=space+r
    print("+",r,"=",space)
    reverse//=10