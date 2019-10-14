# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # ** .5 gets a number's square root
        return (num ** 0.5).is_integer()