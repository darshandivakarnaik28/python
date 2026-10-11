a=[10,-5,6,-4,11,-20,7,-12,0]

def swap(i,j):
    if(i!=j):
        a[i]=a[i]^a[j]
        a[j]=a[i]^a[j]
        a[i]=a[i]^a[j]

def partition(a,l,r):
    i=l-1
    j=l
    while(j<=r):
        if(a[j]<a[r]):
            i+=1
            swap(i,j)
        j+=1
    j-=1
    i+=1
    swap(i,j)
    return i

def quicksort(a,l,r):
    if(l<r):
        i=partition(a,l,r)
        quicksort(a,l,i-1)
        quicksort(a,i+1,r)
        

print("Array before sort: ",a)
quicksort(a,0,len(a)-1)
print("Array after sort: ",a)