# https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    # tests for edge cases
    if nums[0] >= target:
      return 0
    elif nums[-1] < target:
      return len(nums)
    elif nums[-1] == target:
      return len(nums) - 1
    # implements binary search for O(log n) solution
    else:
      # start off assuming the lowest idx is 0 and highest is nums length - 1
      lowest_idx: int = 0
      highest_idx: int = len(nums) - 1

      while True:
        # get the middle idx to cut our search in half immediately
        # lowest and highest idx update based on whether target is higher or lower than the middle, respectively
        middle_idx: int = (lowest_idx + highest_idx) // 2
        if target > nums[middle_idx]:
          lowest_idx = middle_idx
          if target < nums[middle_idx + 1]:
            return middle_idx + 1
          continue
        elif target < nums[middle_idx]:
          highest_idx = middle_idx
          if target > nums[middle_idx - 1]:
            return middle_idx
          continue
        else:
          return middle_idx