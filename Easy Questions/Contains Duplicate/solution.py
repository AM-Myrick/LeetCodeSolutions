# https://leetcode.com/problems/contains-duplicate/
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: true

# Example 2:
# Input: [1,2,3,4]
# Output: false

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List, Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set and add the numbers
        # return true if a number has already been added
        # return false if the loop over the list completes
        copy: Set = set()
        for num in nums:
            if num in copy:
                return True
            copy.add(num)
        return False