# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
      return n
    lowest: int = 0
    highest: int = n
    while True:
      # get the middle to cut our search in half immediately
      # lowest and highest update based on whether or not the middle is a bad version
      middle: int = (lowest + highest) // 2
      if isBadVersion(middle):
        if isBadVersion(middle - 1) == False:
          return middle
        highest = middle
      else:
        if isBadVersion(middle + 1) == True:
          return middle + 1
        lowest = middle
        