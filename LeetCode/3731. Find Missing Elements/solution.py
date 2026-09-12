class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        res=[]
        for i in range(num[0],num[-1]+1):
            if i in num:
                continue
            else:
                res.append(i)
        
        return res