# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=input().split()
b=input().split()
A,B=[],[]
for i in a:
    if i.isdigit():
        A.append(int(i))
for j in b:
    if j.isdigit():
        B.append(int(j))
result=list(product(A,B))
for s in result:
    print(s,end=" ")






