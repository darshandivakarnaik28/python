class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for j,i in enumerate(words):     
            if x in i:
                l.append(j)
        return l