def array_diff(a, b):
    s = a.copy()
    for i in b:
        while i in s:
            s.remove(i)
    return s