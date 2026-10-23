n=int(input("Enter a number to generate fibonacci series: "))
a=[0]*(n+1)
a[0]=0
a[1]=1
for i in range(2,n+1):
    a[i]=a[i-1]+a[i-2]
print(a)