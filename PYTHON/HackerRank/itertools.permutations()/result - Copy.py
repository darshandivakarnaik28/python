# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s=input().split()
p=s[0]
n=s[1]
result=tuple (list(permutations(p,int(n))))
res=sorted(result)
for i in res:
    print("".join(i))

