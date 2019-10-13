# https://leetcode.com/problems/valid-anagram/
from collections import Counter
    
class Solution:
    def anagramHelper(self, s: Counter, t: Counter) -> bool:
        for key, value in t.items():
            if key not in s or s[key] > value:
                return False
        return True
    def isAnagram(self, s: str, t: str) -> bool:
        # converts the strings to a {letter: count} structure
        # returns a helper function's value so that
        # whichever counter is longer is input second
        # and iterated over for comparison
        s_counter, t_counter = Counter(s), Counter(t)
        return self.anagramHelper(s_counter, t_counter) if len(t_counter) >= len(s_counter) else self.anagramHelper(t_counter, s_counter)