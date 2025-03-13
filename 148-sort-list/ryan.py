# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 228ms (75.63%), Memory: 69.36MB (6.05%)
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        linked_list = []
        curr = head
        while curr:
            linked_list.append(curr.val)
            curr = curr.next
        linked_list.sort()
        head = ListNode()
        curr = head
        for i in range(len(linked_list)):
            curr.val = linked_list[i]
            if i + 1 < len(linked_list):
                curr.next = ListNode()
                curr = curr.next 
        return head
        
