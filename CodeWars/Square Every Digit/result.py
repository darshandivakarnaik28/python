def square_digits(num):
    s=''
    num=str(num)
    for i in num:
        s+=str(int(i)**2)
    return int(s)
