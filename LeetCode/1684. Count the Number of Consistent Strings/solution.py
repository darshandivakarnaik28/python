class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for j in words:
            a=True
            for i in j:
                if i in allowed and a==True:
                    a=True
                else:
                    a=False
            if a==True:
                count+=1
        return count