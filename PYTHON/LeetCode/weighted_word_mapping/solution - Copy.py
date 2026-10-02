class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total_weight = sum(weights[ord(ch) - ord('a')] for ch in word)
            val = total_weight % 26
            mapped_char = chr(ord('z') - val)
            res.append(mapped_char)
            
        return "".join(res)