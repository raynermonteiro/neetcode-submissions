class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slowP = fastP = head
        while fastP and fastP.next:
            fastP = fastP.next.next
            slowP = slowP.next
        
        # 2. Split the list and reverse the second half
        currP = slowP.next     # FIX 1: Start reversing from slowP.next
        slowP.next = None      # FIX 2: Break the link between the halves
        prevP = None

        while currP:
            nextP = currP.next
            currP.next = prevP
            prevP = currP
            currP = nextP
        
        # 3. Merge the two halves
        first, second = head, prevP
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2