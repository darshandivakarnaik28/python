class Solution:
    def convert(self, s: str) -> str:
        words=s.split(" ")
        res=""
        for word in words:
            if word:
                res+=word[0].upper()+word[1:]
            res+=" "
        return res
            