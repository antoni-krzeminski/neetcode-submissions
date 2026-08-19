# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next

        steps = counter - n

        # If the head itself needs to be removed
        if steps == 0:
            return head.next

        curr = head
        counter = 0
        while curr:
            counter += 1
            if counter == steps:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next

        return head
