# https://leetcode.com/problems/remove-element/
from typing import List
class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    while True:
      try:
        nums.remove(val)
      except:
        return len(nums)