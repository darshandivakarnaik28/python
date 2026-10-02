# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n=input().split()
a=int(n[0])
b=int(n[1])
D=defaultdict(list)
for i in range(1,a+1):
    word=input().strip()
    D[word].append(i)
for i in range(b):
    word=input().strip()
    if word in D:
        print(*D[word])
    else:
        print(-1)
