# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    # check if it's possible for duplicates to exist
    if len(nums) == 0 or len(nums) == 1:
      return len(nums)
    # remove the index as long as it's equal to the next index
    i, j = 0, 1
    while i < len(nums) - 1:
      if nums[i] == nums[j]:
        nums.pop(i)
        continue
      i, j = i + 1, j + 1
    return j