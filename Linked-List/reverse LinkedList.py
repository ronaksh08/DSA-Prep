# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Iterative approach using two pointers
        # T: O(n) and M:O(1)
        # if not head:
        #     return None

        # prev,  curr = None, head

        # while(curr):

        #     nex = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nex

        # return prev

        #Recursive approach
        # T : O(n) and M : O(n)

        if not head:
            return None
        newHead = head
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead





