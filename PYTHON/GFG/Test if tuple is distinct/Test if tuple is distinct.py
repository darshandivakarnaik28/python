arr = tuple(map(int, input().split()))
distinct={}
for i in arr:
    if i not in distinct:
        distinct[i]=1
    else:
        distinct[i]+=1
count=0
for i in distinct:
    if distinct[i]>1:
        count=1
if count==1:
    print("False")
else:
    print("True")
