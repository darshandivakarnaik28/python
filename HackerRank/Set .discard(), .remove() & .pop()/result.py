n = int(input())
s = set(map(int, input().split()))
n1=int(input())
for i in range(n1):
    o=input().split()
    op=str(o[0])
    if len(o)==2:
        num=int(o[1])
        if op=="discard":
            s.discard(num)
        if op=="remove":
            s.remove(num)
    else:
        s.pop()
count=0
for i in s:
    count+=i
print(count)
