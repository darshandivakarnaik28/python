import numpy as np


class Solution:

  def searchElement(self, arr, target):
    # Check if target matches any element in the 2D array
    return bool(np.any(arr == target))