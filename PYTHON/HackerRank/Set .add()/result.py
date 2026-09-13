# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
t=set()
for  i in range(n):
    s=input()
    t.add(s)
count=0
for j in t:
    count+=1
print(count)
    
