# https://leetcode.com/problems/length-of-last-word/
from typing import List
class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    # split s into empty strings and words
    copy: List[str] = s.split(" ")
    # removes empty strings
    while "" in copy:
      copy.remove("")
    return 0 if copy == [] else len(copy[-1])