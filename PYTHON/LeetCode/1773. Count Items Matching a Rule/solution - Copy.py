class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        l=[]
        for item in items:
          d={}
          d["type"]=item[0]
          d["color"]=item[1]
          d["name"]=item[2]
          l.append(d)
        count=0
        for key in l:
          if key[ruleKey]==ruleValue:
            count+=1
          
        return count
