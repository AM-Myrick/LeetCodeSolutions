# https://leetcode.com/problems/reverse-string/
class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # i references first element in s, j references the last element in s
    i, j = 0, len(s) - 1
    # loop only runs until all values have been swapped
    while j > i:
      # swap the values, increment i and decrement j
      s[i], s[j] = s[j], s[i]
      i, j = i + 1, j - 1
    