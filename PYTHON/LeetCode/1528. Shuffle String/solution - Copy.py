class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=""
        for i in range(len(s)):
            if i in indices:
                j=indices.index(i)
                res+=s[j]
        return res
        
                    
                    
