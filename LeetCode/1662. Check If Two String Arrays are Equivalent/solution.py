class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1="".join(word for word in word1)
        word2="".join(word for word in word2)
        if word1==word2:
            return True
        else:
            return False