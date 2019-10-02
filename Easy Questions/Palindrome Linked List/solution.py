# https://leetcode.com/problems/palindrome-linked-list/
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    copy: List[int] = []
    # update head to next node and add its value to copy
    while head != None:
      copy.append(head.val)
      head = head.next
    # check if copy equals copy reversed
    return copy == copy[::-1]