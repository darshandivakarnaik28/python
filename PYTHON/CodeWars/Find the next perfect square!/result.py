import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq>0:
        s=math.sqrt(sq)
        if sq%s==0:
            return int((s+1)**2)

        return -1
    else:
        return None