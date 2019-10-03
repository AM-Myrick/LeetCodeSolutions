# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # counts number of times each element appears in list
    count = Counter(nums)
    # list comprehension that gets the value of the k most common elements
    return [num[0] for num in count.most_common(k)]