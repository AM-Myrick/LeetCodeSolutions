# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        value_check = set()
        arr_counter = Counter(arr)
        
        for v in arr_counter.values():
            if v in value_check:
                return False
            value_check.add(v)
        return True