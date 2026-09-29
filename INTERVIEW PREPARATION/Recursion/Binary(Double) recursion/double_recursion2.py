def add_(n,add):
    if n>0:
        s=f"sum of {n}+{add}="
        add+=n
        n-=1
        print(f"{s}{add}")
        add_(n,add)
        add_(n,add)
add_(3,0)
