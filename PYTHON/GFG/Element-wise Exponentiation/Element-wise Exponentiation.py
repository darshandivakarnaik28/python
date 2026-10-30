class Solution:
    def elementWisePower(self, arr, e):
        result=[]
        for i in arr:
            result.append(i**e)
        return np.array(result)
            
