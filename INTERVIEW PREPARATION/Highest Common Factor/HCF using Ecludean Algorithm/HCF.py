def get_hcf(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return (a)
a=int(input("Enter a :"))
b=int(input("Enter b :"))
print(get_hcf(a,b))