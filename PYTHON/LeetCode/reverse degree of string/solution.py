class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            reverse = 26 - (ord(char) - ord("a"))
            total += reverse * i
        return total