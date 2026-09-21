def get_hcf(a,b):
    hcf=0
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
a=int(input("Enter a a :"))
b=int(input("Enter a b :"))
print(get_hcf(a,b))
