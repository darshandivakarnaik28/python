def longest(a1, a2):
    s=a1+a2
    n=set()
    for i in s:
        n.add(i)
    return "".join(sorted(n))