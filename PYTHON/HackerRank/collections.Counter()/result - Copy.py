# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
l=input().split()
l=map(int,l)
l=Counter(l)
c=int(input())
total=0
for i in range(c):
    s=input().split()
    size=int(s[0])
    price=int(s[1])
    if l[size] >0:
        total+=price
        l[size]-=1
print(total)
        
    
