# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
from typing import List
from collections import Counter
class Solution:
  def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    result = []
    arr_counter = Counter(arr1)
    for num in arr_counter.keys():
      if num in arr2 and num in arr3:
        result.append(num)
    return result