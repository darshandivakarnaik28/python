def create_phone_number(n):
    s=""
    m=""
    l=""
    for i,_ in enumerate(n):
        print(i)
        if i<3:
            s+=str(n[i])
        elif i<6:
            m+=str(n[i])
        else:
            l+=str(n[i])
    s="("+s+")"+" "+m+"-"+l
    return s