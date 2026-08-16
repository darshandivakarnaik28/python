if __name__ == '__main__':
    s = input()
    if 0<len(s)<1000:
        if any(c.isalnum() for c in s):
            print("True")
        else:
            print("False")
        if any(c.isalpha() for c in s):
            print("True")
        else:
            print("False")
        if any(c.isdigit() for c in s):
            print("True")
        else:
            print("False")
        if any(c.islower() for c in s):
            print("True")
        else:
            print("False")
        if any(c.isupper() for c in s):
            print("True")
        else:
            print("False")    
            
