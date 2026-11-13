class MySet:
    
    # Insert an element into the set.
    def insert(self, s, x):
        s.add(x)
        

    # Remove an element from the set if it exists.
    def erase(self, s, x):
        s.discard(x)
    # Return the number of distinct elements in the set.
    def size(self, s):
        return len(s)

    # Return 1 if the element exists; otherwise, return -1.
    def find(self, s, x):
        if x in s:
            return 1
        else:
            return -1