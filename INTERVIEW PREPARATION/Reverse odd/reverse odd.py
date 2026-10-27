n=int(input("Enter a range to generate Reverse odd number : "));
n=int(n/2)
print("Before Reverse:",end="")
for i in range(1,n+1):
    print(i+i-1,end=" ")

print("\nAfter Reverse:",end="")
for i in range(1,n+1):
    print(n-i+n-i+1,end=" ")

