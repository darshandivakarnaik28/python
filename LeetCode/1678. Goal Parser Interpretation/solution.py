class Solution:
    def interpret(self, command: str) -> str:
        s=""
        for i ,j in enumerate(command):
            if "A"<=j<="Z":
                s+=j
            elif j=="(" and command[i+1]==")":
                s+="o"
            elif j=="(" or j==")":
                continue
            else:
                s+=j
        return s
        