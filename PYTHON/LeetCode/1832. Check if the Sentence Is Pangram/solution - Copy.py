class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence=len(set(sentence))
        if sentence==26:
            return True
        else:
            return False
        