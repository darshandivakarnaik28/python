def printIncreasingPower(x):
    #code here
    # Loop to jump in powers of 2
    i=1
    j=1
    while(j<x):
        #code here
        j=i**2
        if j<=x:
            print ( j, end = " ")
        i+=1