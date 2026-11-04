class Solution:
    def booleanOperations(self, a: bool, b: bool) -> str:
        res_and = a and b
        res_or = a or b
        res_not = not a
        return f"{str(res_and).lower()} {str(res_or).lower()} {str(res_not).lower()}"