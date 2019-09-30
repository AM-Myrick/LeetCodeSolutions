# https://leetcode.com/problems/reverse-integer/
class Solution:
  def reverse(self, x: int) -> int:
    if len(str(x)) == 1:
      return x
      
    # create a positive copy of the integer and cast it as a list
    copy = abs(x)
    copy = list(str(copy))
      
    # remove leading zeroes and reverse the list
    while int(copy[len(copy) - 1]) == 0:
      copy.pop()
    copy = copy[::-1]
      
    # if the reversed integer overflows, return 0 else, return the reversed integer
    if x < 0:
      if int("-" + (''.join(str(i) for i in copy))) < -2**31:
        return 0
      return int("-" + (''.join(str(i) for i in copy)))
    if int(''.join(str(i) for i in copy)) >= 2**31:
      return 0
    return int(''.join(str(i) for i in copy))
      