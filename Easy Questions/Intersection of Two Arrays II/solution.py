# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_counter = Counter(nums1)
    nums2_counter = Counter(nums2)
    result: List = []
    for key, value in nums1_counter.items():
      if key in nums2_counter and value <= nums2_counter[key]:
        while value:
          result.append(key)
          value -= 1
      elif key in nums2_counter and value > nums2_counter[key]:
        while nums2_counter[key]:
          result.append(key)
          nums2_counter[key] -= 1
    return result