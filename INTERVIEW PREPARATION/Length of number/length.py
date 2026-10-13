n=int(input("Enter a number: "))
count=0
while(n!=0):
    r=n%10
    n=n//10
    count+=1
print("Length of a number is: ",count)