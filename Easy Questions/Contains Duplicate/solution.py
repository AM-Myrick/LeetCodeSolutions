from typing import List, Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a dict and add the numbers
        # return true if a number has already been added
        # return false if the loop over the list completes
        copy: Set = set()
        for num in nums:
            if num in copy:
                return True
            copy.add(num)
        return False