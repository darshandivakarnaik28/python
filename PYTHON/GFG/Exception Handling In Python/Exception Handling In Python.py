def find_minimum(a, b):
    # code here  
    add=a+b
    sub=a-b
    mul=a*b
    try:
        if b==0:
            div=b//a
        else:
            div=a//b
    except ZeroDivisionError:
        return "Division by zero"
    return min(add,sub,mul,div)