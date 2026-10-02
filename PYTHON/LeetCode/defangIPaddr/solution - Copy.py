class Solution:
    def defangIPaddr(self, address: str) -> str:
        p=""
        for i in  address:
            if i =='.':
                p+="[.]"
            else:
                p+=str(i)
        return p
