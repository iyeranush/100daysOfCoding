class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        1 -> 2 -> 3 -> 4 -> 5
        n=1, l = 5 -> length_to_traverse=4
        n=2, l=2 -> traverse=0
        """
        length = self.calculateLength(head)
        length_to_traverse = length - n
        if length_to_traverse == 0:
            head = head.next
        else:
            i = 1
            curr = head
            while i < length_to_traverse:
                curr = curr.next
                i += 1
            curr.next = curr.next.next
        return head

    def calculateLength(self, head):
        if not head:
            return 0
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def removeNthFromEndOnePass(self, head, n):
        # Using this concept: if n= 4 in length = 10
        # It means we need to essentially move 6 places.
        # But if we do not know 10, the way we can solve this is:
        # Have 2 variables fast and slow
        # let fast get a head start and move 4 places
        # Now let start and fast move equally such that fast.next = None

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

solution = Solution()


assert solution.removeNthFromEnd(l1, 5).val == 2 # 2->3->4->5
assert solution.removeNthFromEnd(l2, 1).val == 2 # 2->3->4
assert solution.removeNthFromEnd(l2, 2).val == 2 # 2->3
assert solution.removeNthFromEnd(l2, 1).val == 2 # 2
assert solution.removeNthFromEnd(l2, 1) == None # None
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

assert solution.removeNthFromEndOnePass(l1, 5).val == 2
assert solution.removeNthFromEndOnePass(l2, 1).val == 2
assert solution.removeNthFromEndOnePass(l2, 2).val == 2
assert solution.removeNthFromEndOnePass(l2, 1).val == 2
assert solution.removeNthFromEndOnePass(l2, 1) == None
