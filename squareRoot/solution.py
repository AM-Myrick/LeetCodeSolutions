# https://leetcode.com/problems/sqrtx/
import math
class Solution:
  def mySqrt(self, x: int) -> int:
    return math.floor(x ** .5)