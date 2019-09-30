# https://leetcode.com/problems/palindrome-number/
class Solution:
  def isPalindrome(self, x: int) -> bool:
    # negatives can't be palindromes
    if x < 0:
      return False
    # convert x to a string since ints aren't iterable, convert to a list and reverse it
    reverse = list(str(x))[::-1]
    
    # return the boolean resulting from x == reversed x
    return x == int(''.join(reverse))