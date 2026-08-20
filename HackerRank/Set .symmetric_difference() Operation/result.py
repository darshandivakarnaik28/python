# Enter your code here. Read input from STDIN. Print output to STDOUT\\
n1=input()
l1=set(input().split())
n2=input()
l2=set(input().split())
print(len(l1.symmetric_difference(l2)))
