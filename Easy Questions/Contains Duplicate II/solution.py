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
            if num in copy and abs(copy[num] - idx) <= k:
                return True
            copy[num] = idx
        return False
        