# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head

        n = 1
        tail = ListNode()
        temp = tail
        tail.next = head
        
        while head.next != None:
            n += 1
            head = head.next

        head.next = temp.next
        head = head.next
        k = k % n
        for _ in range(n - k -1):
            head = head.next
        result = head.next
        head.next = None
        return result
