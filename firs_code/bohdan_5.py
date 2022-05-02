class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        S = set()
        while head:
            if id(head) in S: return True
            S.add(id(head))
            head = head.next
        return False