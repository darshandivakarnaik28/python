Given two positive integers a and b, perform a right bitwise shift of a by b positions, followed by a left bitwise shift of a by b positions. Print both results separated by a space, followed by new line.

Examples:

Input: a = 5, b = 2
Output: 1 20
Explanation: 5 in binary is 101. Shifting right by 2 gives 001, which equals 1. Shifting left by 2 gives 10100, which equals 20. 
Input: a = 4, b = 1
Output: 2 8
Explanation: 4 in binary is 100. Shifting right by 1 gives 010, which equals 2. Shifting left by 1 gives 1000, which equals 8. 
Constraints:

1 ≤ a ≤ 100
1 ≤ b ≤ 10