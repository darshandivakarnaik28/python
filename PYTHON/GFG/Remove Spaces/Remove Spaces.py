class Solution:
    def removeSpaces(self, s):
        res=""
        for ch in s:
            if ch!=" ":
                res+=ch
        return res
                