class Solution:

  def addBinary(self, a: str, b: str) -> str:
    result = []
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    # Loop from the rightmost digits to the leftmost
    while i >= 0 or j >= 0 or carry:
      total = carry

      if i >= 0:
        total += int(a[i])
        i -= 1

      if j >= 0:
        total += int(b[j])
        j -= 1

      # Append the current bit (total % 2) to the result list
      result.append(str(total % 2))
      # Update carry for the next position
      carry = total // 2

    # Since we appended from right to left, reverse and join
    return "".join(reversed(result))