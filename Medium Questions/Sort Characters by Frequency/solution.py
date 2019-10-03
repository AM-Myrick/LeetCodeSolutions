# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter
class Solution:
  def frequencySort(self, s: str) -> str:
    # counts number of times each element appears in s
    count = Counter(s)
    # adds every letter to a list the number of times it appears in s
    # by order of frequency, then converts list to str
    return "".join([letter * frequency for letter, frequency in count.most_common()])