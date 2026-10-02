def accum(st):
    s=""
    for k,i in enumerate(st):
        if i!=i.upper():
            s+=f"{i.upper()}{i*k}-"
        else:
            s+=i+i.lower()*k+"-"
    return s.rstrip('-')