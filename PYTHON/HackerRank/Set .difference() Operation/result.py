# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
l1=set(input().split())
n2=int(input())
l2=set(input().split())
print(len(l1.difference(l2)))

