class Solution:
    def longest(self, arr):
        longest_word = ""
        for ch in arr:
            if len(ch) > len(longest_word):
                longest_word = ch

        return longest_word