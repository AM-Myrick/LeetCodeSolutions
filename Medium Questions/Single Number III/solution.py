# https://leetcode.com/problems/single-number-iii/
from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count the number of times each element appears
        nums_counter = Counter(nums)
        result = []
        # iterate over the dict and append the key to result
        # if the value is equal to 1
        # return when length of result is equal to 2
        for key, value in nums_counter.items():
            if value == 1:
                result.append(key)
                if len(result) == 2:
                    return result