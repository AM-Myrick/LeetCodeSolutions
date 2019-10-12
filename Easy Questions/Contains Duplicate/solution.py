from typing import List, Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set data structure removes duplicates
        # then return whether or not the length of the set
        # and the original list are the same
        copy: Set = set(nums)
        return len(copy) != len(nums)