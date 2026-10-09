a=[10,5,98,60,32,40,100]
for i in range(0,len(a)-1,1):
    for j in range(i+1,len(a)-1,1):
        if a[i]>a[j]:
             a[i]=a[i]^a[j]
             a[j]=a[i]^a[j]
             a[i]=a[i]^a[j]
print(a)