class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        k=s[k-1::-1]+s[k::]
        return k