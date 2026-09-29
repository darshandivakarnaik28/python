def hello(n):
    if n>0:
        print(n)
        n-=1
        hello(n)
        hello(n)
hello(3)