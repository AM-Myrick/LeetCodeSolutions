# https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    # check if target exists in list or if zeroth element is > target
    if target in nums:
      return nums.index(target)
    if nums[0] > target:
      return 0
    # finds where target should be inserted
    for idx, num in enumerate(nums):
      if idx == len(nums) - 1 or num < target and nums[idx + 1] > target:
        return idx + 1