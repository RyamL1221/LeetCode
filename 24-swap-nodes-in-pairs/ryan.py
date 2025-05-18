# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 0ms (100.00%), Memory: 12.44MB (64.22%)
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev  = dummy      # node before the current pair
        curr  = head       # first node of the current pair

        while curr and curr.next:
            nxt = curr.next            # second node of the pair

            # swap curr and nxt
            curr.next = nxt.next
            nxt.next  = curr
            prev.next = nxt

            # move pointers forward
            prev = curr
            curr = curr.next           # start of the next pair

        return dummy.next
