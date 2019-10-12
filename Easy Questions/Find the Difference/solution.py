# https://leetcode.com/problems/find-the-difference/
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # converts s & t to a dict {letter: number of times it appears}
        s_counter, t_counter = Counter(s), Counter(t)
        
        # iterates over the keys and checks if a letter isn't in s
        # or if it appears in t more often than in s
        for letter in t_counter.keys():
            if letter not in s_counter or s_counter[letter] != t_counter[letter]:
                return letter