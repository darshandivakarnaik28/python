class Solution:
    def concatenatedString(self, s1, s2):
        res=""
        for ch in s1:
            if ch not in s2:
                res+=ch
        for ch in s2:
            if ch not in s1:
                res+=ch
        if res:
            return res
        else:
            return "-1"