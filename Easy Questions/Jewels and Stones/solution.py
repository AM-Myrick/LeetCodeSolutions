# https://leetcode.com/problems/jewels-and-stones/
from collections import Counter
class Solution:
  def numJewelsInStones(self, J: str, S: str) -> int:
    # counts the number of times each stone appears in S
    stone_counter = Counter(S)
    jewels: int = 0
    # counts the number of times each jewel appears in stone_counter
    for jewel in J:
      jewels += stone_counter[jewel]
    return jewels