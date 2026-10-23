Given two integers a and b, return the minimum value obtained from performing any of the following arithmetic operations between a and b: addition (+), subtraction (-), multiplication (*), and floor division (//).
Make sure to use exception handling to manage any potential division by zero errors.

Note: If division by zero is attempted, handle the exception and exclude the division operation from consideration.

Examples:

Input: a = 5, b = -5
Output: -25
Explanation:
The results of the operations are:
5+(−5)=0
5−(−5)=10
5×(−5)=−25
5/(−5)=−1
The minimum value is -25.
Input: a = 5, b = 0
Output: 0
Explanation:
The results of the operations are:
5+0=5
5−0=5
5×0=0
5/0 raises a "Division by zero" exception.
Thus, the minimum value among valid operations is 0.
Constraints:
-10 ≤ a, b ≤ 10 