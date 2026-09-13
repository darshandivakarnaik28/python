# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
l1=set(input().split())
n2=int(input())
l2=input().split()
num=l1.intersection(l2)
print(len(num))
