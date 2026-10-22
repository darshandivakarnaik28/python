class Solution:
    def reverseArray(self, arr):
        start=0
        end=len(arr)-1
        while start<end:
            arr[start]=arr[start]^arr[end]
            arr[end]=arr[start]^arr[end]
            arr[start]=arr[start]^arr[end]
            start+=1
            end-=1