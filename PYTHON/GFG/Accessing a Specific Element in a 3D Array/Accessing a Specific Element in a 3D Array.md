Given a 3D NumPy array arr and indices (x, y, z), access and return the element present at the specified index (x, y, z).

Example:
Input: arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), index = (1, 0, 1)
Output: 6
Explanation: The element at index (1, 0, 1) is 6. Here, 1 selects the second 2D block, 0 selects the first row within that block, and 1 selects the second element of that row.
Input: arr = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]]), index = (0, 1, 0)
Output: 30
Explanation: The element at index (0, 1, 0) is 30. Here, 0 selects the first 2D block, 1 selects the second row within that block, and 0 selects the first element of that row.