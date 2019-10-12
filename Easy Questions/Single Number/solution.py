# https://leetcode.com/problems/single-number/
from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count the number of times each element appears
        nums_counter = Counter(nums)
        # iterate over the dict and return the key where
        # value is equal to 1
        for key, value in nums_counter.items():
            if value == 1:
                return key