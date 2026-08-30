class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=set()
        for i in sentences:
            s=i.split()
            l=len(s)
            res.add(l)
        return max(res)