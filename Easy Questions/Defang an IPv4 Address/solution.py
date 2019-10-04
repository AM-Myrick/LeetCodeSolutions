# https://leetcode.com/problems/defanging-an-ip-address/
from typing import List
class Solution:
  def defangIPaddr(self, address: str) -> str:
    copy: List[str] = list(address)
    for idx, char in enumerate(copy):
      if char == ".":
        copy[idx] = "[.]"
    return "".join(copy)