class Solution:
    def firstOccurence(self,txt,pat):
        if pat in txt:
            return txt.find(pat)
        else:
            return -1