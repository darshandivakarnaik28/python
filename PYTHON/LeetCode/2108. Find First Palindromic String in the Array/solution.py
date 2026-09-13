class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            rev=word[::-1]
            if rev==word:
                return word
        return ""