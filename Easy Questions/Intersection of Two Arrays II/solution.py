# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # create a function to ensure the array with less elements is iterated over
    def find_intersects(first_nums, second_nums):
      result = []
      for key, value in first_nums.items():
        if key in second_nums and value <= second_nums[key]:
          while value:
            result.append(key)
            value -= 1
        elif key in second_nums and value > second_nums[key]:
          while second_nums[key]:
            result.append(key)
            second_nums[key] -= 1
      return result
    
    nums1_counter = Counter(nums1)
    nums2_counter = Counter(nums2)
    return find_intersects(nums1_counter, nums2_counter) if len(nums1_counter) <= len(nums2_counter) else find_intersects(nums2_counter, nums1_counter)
    
    