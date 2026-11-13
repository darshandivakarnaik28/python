Given two integers a and b, perform each of the following arithmetic operations: addition (+), subtraction (-), multiplication (*), and floor division (/). Return the minimum value obtained from these operations as a.

Do not consider division while finding minimum if b is 0.
You must use exception handling to avoid division by 0.
Examples:

Input: a = 5, b = -5
Output: -25
Explanation:
5+(-5) = 0,
5-(-5) = 10,
5*(-5) = -25,
5/(-5) = -1.
Minimum of all is 5*(-5) = -25.
Input: a = 5, b = 0
Output: 0
Explanation:
5+0 = 5,
5-0 = 5,
5*0 = 0,
5/0 = Undefined (Creates Arithmetic Exception so we ignore this).
Minimum of all is 5*0 = 0.
Constraints:

-103 ≤ a, b ≤ 103