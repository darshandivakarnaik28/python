def add_(n,sum):
    if n>0:
        s=f"sum of {n}+{sum}="
        sum=sum+n
        n-=1
        print(f"{s}{sum}")
        add_(n,sum)               
add_(3,0)
