class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        in_pair = False
        
        for char in s:
            if char == '|':
                in_pair = not in_pair
            elif char == '*' and not in_pair:
                ans += 1
                
        return ans