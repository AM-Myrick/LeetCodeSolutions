# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idx, num in enumerate(nums):
      target_value = target - num
      if target_value in nums:
        target_idx = nums.index(target_value)
        if idx != target_idx:
          return [idx, target_idx]
      