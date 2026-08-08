# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = None # Initialize Previous as None
        currHead = head # Make Current Head as the first Node in the List

        while currHead:
            temp = currHead.next # Store the next Node in Temp
            currHead.next = prevHead # Reverse Pointer of CurrenHead to Previous
            prevHead = currHead # Make Previous the currentHead
            currHead = temp # Make currentHead the next Head which is store in temp [Move current forward]

        return prevHead



        