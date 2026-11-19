# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        current1 = l1
        current2 = l2
        
        resultHead = None
        resultTail = None
        carry = 0

        while current1 is not None or current2 is not None or carry:
            total = carry
            if current1 is not None:
                total+=current1.val
                current1 = current1.next
            
            if current2 is not None:
                total+=current2.val
                current2 = current2.next

            digit = total%10
            carry = total//10

            newNode = ListNode(digit)

            if resultHead is None:
                resultHead = newNode 
                resultTail = newNode
            else:
                resultTail.next = newNode
                resultTail = newNode

        return resultHead
        