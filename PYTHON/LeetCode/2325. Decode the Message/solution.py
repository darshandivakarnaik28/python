class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s=[]
        d={" ":" "}
        for i in key:
            if i not in s and i!=" ":
                s.append(i)
        k=97
        res=""
        for i in s:
            d[i]=chr(k)
            k+=1
        for i in message:
            res+=d[i]
        return res