class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st=""
        s=s.split()
        return " ".join(s[0:k])