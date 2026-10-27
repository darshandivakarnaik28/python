n=int(input("Enter a number to generate triangle : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()