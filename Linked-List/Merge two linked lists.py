# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # list3 = ListNode()
        # firstnode = list3

        # while(list1 and list2):

        #     if list1.val <= list2.val:
        #         firstnode.next = list1
        #         list1 = list1.next
        #     else:
        #         firstnode.next = list2
        #         list2 = list2.next
        #     firstnode = firstnode.next
            
        # if list1:
        #     firstnode.next = list1
        # if list2:
        #     firstnode.next = list2

        # return list3.next

        # Recursive approach

        if not list1 and not list2:
            return None

        if not list1:
            return list2
        if not list2:
            return list1

        
        if list1.val <= list2.val :
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
        
                                



        
