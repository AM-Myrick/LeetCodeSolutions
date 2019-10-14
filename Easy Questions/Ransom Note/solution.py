# https://leetcode.com/problems/ransom-note/
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # get a count of the number of times a letter appears in each parameter
        note_counter, magazine_counter = Counter(ransomNote), Counter(magazine)
        # subtract the number of letters in note from the number of letters in magazine
        magazine_counter.subtract(note_counter)
        
        # if there's a negative value, the magazine doesn't have enough letters
        # otherwise, return True
        for v in magazine_counter.values():
            if v < 0:
                return False
        return True