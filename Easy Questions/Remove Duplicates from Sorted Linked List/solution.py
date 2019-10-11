# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        curr: ListNode = head
        # if the current pointer's value is equal to it's next node's value
        # change the next node to it's own next node
        while curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            curr = curr.next
        return head