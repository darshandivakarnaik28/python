def print_rangoli(size):
    width=4*size-3
    for row in range (size,0,-1):
        s=[]
        for i in range(size,row-1,-1):
            s.append(chr(i+96))
        for i in range(row+1,size+1):
            s.append(chr(i+96))
        line="-".join(s)
        print(line.center(width,"-"))
        
    for row in range(2,size+1):
        s=[]
        for i in range(size,row-1,-1):
            s.append(chr(i+96))
        for i in range(row+1,size+1):
            s.append(chr(i+96))
        line="-".join(s)
        print(line.center(width,"-"))
        
            
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)