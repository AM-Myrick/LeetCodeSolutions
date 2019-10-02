# https://leetcode.com/problems/valid-palindrome/
class Solution:
  def isPalindrome(self, s: str) -> bool:
    # list comprehension to lowercase each alphanumeric character in the string
    # and add it to a list
    s = [e.lower() for e in s if e.isalnum()]
    return s == s[::-1]