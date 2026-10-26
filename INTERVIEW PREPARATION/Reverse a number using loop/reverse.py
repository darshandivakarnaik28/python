n=int(input("Enter a range to reverse : "))
print("Before Reverse:",end="")
for i in range(1,n+1):
    print(i,end=" ")
print("\nAfter Reverse:",end="")
for i in range(1,n+1):
    print(n-i+1,end=" ")
    