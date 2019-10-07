# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
from typing import List
class Solution:
  def repeatedNTimes(self, A: List[int]) -> int:
    # create a dict to hold A's values
    A_dict = {}
    # as soon as we find a repeating value, return it
    for num in A:
      if num in A_dict:
        return num
      A_dict[num] = 0