class Solution:
    def isBinary(self, s):
        s=str(s)
        for ch in s:
            if ch!="1" and ch!="0":
                return False
        return True