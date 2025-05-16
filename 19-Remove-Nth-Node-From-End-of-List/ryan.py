# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 0ms (100.00%), Memory: 12.40MB (55.26%)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to head
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move first ahead by n+1 steps
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        # Return the new head
        return dummy.next
        
