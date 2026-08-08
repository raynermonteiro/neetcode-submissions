# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode
        resultHead = resultList

        while list1 and list2:
            if list1.val <= list2.val:
                resultList.next = list1
                list1 = list1.next
            else:
                resultList.next = list2
                list2 = list2.next
            resultList = resultList.next
        
        resultList.next = list1 if list1 else list2

        return resultHead.next