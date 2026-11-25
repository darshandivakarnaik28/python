class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        rev=s[::-1]
        return rev==s