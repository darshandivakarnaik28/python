def remove(s):
    if s!="":
        if s[-1]!="!":
            return s
        else:
            return s[0:-1]
    else:
        return s