# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n=int(n)
m=int(m)
for i in range(1,n,2):
    print((".|."*i).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
    print((".|."*i).center(m,"-"))
