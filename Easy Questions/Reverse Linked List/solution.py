# https://leetcode.com/problems/reverse-linked-list/
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
          return head
        # append all linked list values into a list
        copy: List[int] = []
        while head != None:
          copy.append(head.val)
          head = head.next
        # pop all list values into a new linked list 
        reversed_ll: ListNode = ListNode(copy.pop())
        # create a pointer to the new linked list's head
        reversed_head: ListNode = reversed_ll
          
        while len(copy):
          reversed_ll.next = ListNode(copy.pop())
          reversed_ll = reversed_ll.next
        return reversed_head