# https://leetcode.com/problems/third-maximum-number/
from typing import List
class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    # casts nums as a set to remove duplicates, then casts back to a list and sorts
    nums: List[int] = sorted(set(nums))
    # if there aren't three elements, return the biggest element
    if len(nums) < 3:
      return max(nums)
    # else return the third from last element
    return nums[-3]