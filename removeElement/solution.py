# https://leetcode.com/problems/remove-element/
from typing import List
class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    # while val exists in nums it will be removed, once it doesn't exist nums length is returned
    while True:
      try:
        nums.remove(val)
      except:
        return len(nums)