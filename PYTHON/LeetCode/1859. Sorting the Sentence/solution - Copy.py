class Solution:
    def sortSentence(self, s: str) -> str:
        j=""
        d={}
        for i in s:
          if i.isalpha():
            j+=i        
          elif "0"<=i<="9":
                d[int(i)]=j
                j=""
          else:
            continue
        s=[]
        for i in range(1,len(d)+1):
          s.append(d[i])
        return " ".join(s)

            