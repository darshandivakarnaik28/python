def print_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count
n=int(input("Enter a positive number:"))
count=print_prime(n)
if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")