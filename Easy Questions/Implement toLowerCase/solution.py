# https://leetcode.com/problems/to-lower-case/
class Solution:
  def toLowerCase(self, str: str) -> str:
    return "".join([e.lower() for e in str])    