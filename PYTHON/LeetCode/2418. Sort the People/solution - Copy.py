class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height=sorted(heights)
        height=height[::-1]
        d={}
        for i,j in enumerate(heights):
            d[j]=names[i]
        l=[]
        for i in height:
            l.append(d[i])
        return l