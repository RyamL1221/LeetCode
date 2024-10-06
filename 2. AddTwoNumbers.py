# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        num1 = ""
        num2 = ""
        curr = l1

        while curr != None:
            num1 += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr != None:
            num2 += str(curr.val)
            curr = curr.next

        num1 = num1[::-1]
        num2 = num2[::-1]
        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2
        sum = str(sum)
        sum = sum[::-1]

        root = ListNode(sum[0:1])
        curr = root
        for i in range(1, len(sum)):
            curr.next = ListNode(sum[i:i+1])
            curr = curr.next
        return root

        
        
