def add_(n,sum):
    if n<=3:
        sum+=n
        n+=1
        add_(n,sum)
add_(1,0)
