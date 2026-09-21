def get_swap(a,b):
    print("Before swap a=",a)
    print("Before swap b=",b)
    b=a^b
    a=a^b
    b=b^a
    print("After swap a=",a)
    print("After swap b=",b)
a=int(input("Enter a :"))
b=int(input("Enter b :"))
get_swap(a,b)