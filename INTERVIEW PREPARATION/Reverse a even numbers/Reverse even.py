n=int(input("Enter the range to reverse even numbers : "))
n=int(n/2)
print("Before Reverse :",end="")
for i in range(1,n+1):
    print(i+i,end=" ")
print("\nAfter Reverse :",end="")
for i in range(1,n+1):
    print(n-i+n-i+2,end=" ")