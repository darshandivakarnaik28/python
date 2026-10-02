class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for word in words:
            a=word[0:2]
            if pref==a:
                count+=1 
        return count
        