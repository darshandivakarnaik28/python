from collections import deque

class MyDeque:
    def __init__(self):
        # Initialize your data structure here
        self.dq = deque()

    def addFront(self, x):
        # code here
        self.dq.appendleft(x)

    def addBack(self, x):
        # code here
        self.dq.append(x)

    def removeFront(self):
        # code here
        if not self.dq:
            return -1
        return self.dq.popleft()

    def removeBack(self):
        # code here
        if not self.dq:
            return -1
        return self.dq.pop()

    def elementAtFront(self):
        # code here
        if not self.dq:
            return -1
        return self.dq[0]

    def elementAtBack(self):
        # code here
        if not self.dq:
            return -1
        return self.dq[-1]

    def isEmpty(self):
        # code here
        return len(self.dq) == 0

    def size(self):
        # code here
        return len(self.dq)