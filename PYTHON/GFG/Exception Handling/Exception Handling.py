class Solution:
    def findMin(self, a: int, b: int) -> int:
        results = [a + b, a - b, a * b]

        try:
            results.append(int(a / b))
        except ZeroDivisionError:
            pass

        return min(results)