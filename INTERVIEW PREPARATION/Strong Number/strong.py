n=int(input("Enter a number:"))
sum=0
copy=n
print("sum of ",end="")
while (n!=0):
    r=n%10
    n=n//10
    fact=1
    for i in range(1,r+1):
        fact*=i 
    sum+=fact
    print(f"{i}! ",end="")
print("is =",sum)
if(sum==copy):
    print(copy,"is Strong Number")
else:
    print(copy,"is Not a Strong Number")