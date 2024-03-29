# https://leetcode.com/problems/contains-duplicate-ii/
# Given an array of integers and an integer k, find out whether there are two distinct indices 
# i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create a dict then loops over the list to add values
        # with a structure of {num: index}
        # when coming across a collision, check if its index is <= k
        # if so, return True
        # if not, update the index and continue
        copy: dict = {}
        for idx, num in enumerate(nums):
            if num in copy and idx - copy[num] <= k:
                return True
            copy[num] = idx
        return False
        