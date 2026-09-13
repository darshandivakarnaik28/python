class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=""
        if ch in word:
            j=word.find(ch)
            res=word[j::-1]
            res+=word[j+1::]
        else:
            return word

        return res
            