# Enter your code here. Read input from STDIN. Print output to 
# Enter your code here. Read input from STDIN. Print output to 
from itertools import combinations
s=input().split()
a=str(s[0])
b=s[1]
k=sorted(a)
for i in range(1,int(b)+1):
    result=list(combinations(k,i ))
    res=sorted(result)
    for i in res:
        print("".join(i))

