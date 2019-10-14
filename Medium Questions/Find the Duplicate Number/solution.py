# https://leetcode.com/problems/find-the-duplicate-number/
from collections import Counter
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # create a counter so that every element in nums is counted
        copy = Counter(nums)
        # if a value is greater than 1, return the key
        for k, v in copy.items():
            if v > 1:
                return k