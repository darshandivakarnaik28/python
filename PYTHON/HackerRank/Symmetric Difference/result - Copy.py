# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
s1=input().split()
s1=list(map(int,s1))
n2=int(input())
s2=input().split()
s2=list(map(int,(s2)))
res1=set(s1).difference (set(s2))
res2=set(s2).difference (set(s1))
res=sorted(res1.union(res2))
for k in res:
    print(k)
