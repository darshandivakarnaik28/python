class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=0
        for i in s:
            res+=(abs(s.find(i)-t.find(i)))
        return res