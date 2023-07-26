# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Without using Recursion
        # l3 = ListNode()
        # temp = l3
        # carry= 0
        # while l1 or l2:

        #     if l1:
        #         v1 = l1.val
        #     else:
        #         v1 = 0
        #     if l2:
        #         v2 = l2.val
        #     else:
        #         v2 = 0
        #     v3 = v1 + v2 + carry

        #     carry = int(v3 / 10)
        #     v3 = v3 % 10
            
        #     temp.next = ListNode(v3)

        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        #     temp = temp.next
        # if carry >0:
        #     temp.next = ListNode(carry)

        # return l3.next

        return self.helper(l1,l2,0)

    # with recursion
    def helper(self,l1,l2,carry):

        if not l1 and not l2:
            return ListNode(carry) if carry != 0 else None

        if l1 and l2:

            digit = l1.val + l2.val + carry

            carry = int(digit/10)
            digit = digit % 10
            return ListNode(digit,self.helper(l1.next,l2.next,carry))

        if l1 and not l2:

            digit = l1.val + carry

            carry = int(digit/10)
            digit = digit % 10
            return ListNode(digit,self.helper(l1.next, l2, carry))
        
        elif not l1 and l2:

            digit = l2.val + carry

            carry = int(digit/10)
            digit = digit % 10
            return ListNode(digit,self.helper(l1, l2.next, carry))

        return None
        


        
