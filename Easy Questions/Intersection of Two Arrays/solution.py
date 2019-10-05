from typing import List
class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # remove duplicate numbers from both lists
    nums1 = set(nums1)
    nums2 = set(nums2)
    # returns all numbers appearing in both sets
    return list(nums1.intersection(nums2))