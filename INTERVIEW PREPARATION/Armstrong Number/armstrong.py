n=int(input("Enter a number: "));
copy=n
count=0
while(n!=0):
    r=n%10
    n=n//10
    count+=1
 
n=copy
print("Sum of",end=" ")
sum=0
while(n!=0):
    r=n%10
    sum=sum+r**count
    print(f"{r}**{count}",end=" ")
    n=n//10
print("=",sum)

if(sum==copy):
    print(copy,"is a Armstrong Number")
else:
    print(copy,"is Not an Armstrong Number")

