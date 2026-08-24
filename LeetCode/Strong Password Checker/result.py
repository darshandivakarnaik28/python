import re
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-+])(?!.*(.)\1).{8,}$"
        if re.match(pattern,password):
            return True
        else:
            return False