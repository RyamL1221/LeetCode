# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(n), 0ms (100.00%); Memory: O(1), 18.80MB (37.68%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
