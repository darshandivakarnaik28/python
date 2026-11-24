class Solution:
    def binarySubstring(self, s):
        ones = 0
        count = 0

        for ch in s:
            if ch == '1':
                count += ones
                ones += 1

        return count