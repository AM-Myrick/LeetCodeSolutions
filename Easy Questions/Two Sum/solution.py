# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # iterate over the list and find out if target - current value is within the list
    for idx, num in enumerate(nums):
      target_value = target - num
      if target_value in nums:
        # get the index, ensure it doesn't match the current index, and return both values in list format
        target_idx = nums.index(target_value)
        if idx != target_idx:
          return [idx, target_idx]
      