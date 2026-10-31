Given a 2D NumPy array arr, sort each column of the array independently in ascending order and return the resulting array.

Examples:
Input: arr = np.array([7, 2, 6],[3, 8, 1],[4, 5, 9]])
Output: array([[3, 2, 1], [4, 5, 6], [7, 8, 9]])
Explanation: The columns [7, 3, 4], [2, 8, 5], and [6, 1, 9] are sorted individually. Placing the sorted columns back into the matrix gives the result.
Input: arr = np.array([[9, 4, 7], [3, 8, 2], [6, 1, 5]])
Output: array([[3, 1, 2], [6, 4, 5], [9, 8, 7]])
Explanation: The columns [9, 3, 6], [4, 8, 1], and [7, 2, 5] are sorted individually. Placing the sorted columns back into the matrix gives the result