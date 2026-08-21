# Enter your code here. Read input from STDIN. Print output to STDOUT
r=int(input())
for i in range(r):
    try:
        z=input().split()
        n=int(z[0])
        d=int(z[1])
    
        print (n//d)
    except ZeroDivisionError as e :
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
