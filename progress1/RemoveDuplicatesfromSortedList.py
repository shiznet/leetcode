# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        current = head.next
        previous = head
        while current is not None:
            if previous.val == current.val:
                previous.next = current.next
                current = previous.next
            else:
                previous = current
                current = previous.next
        return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def recurse(self):
        pointer = self
        while pointer is not None:
            print pointer.val
            pointer = pointer.next

if __name__ == "__main__":
    so = Solution()
    root = ListNode(1)
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(4)
    g = ListNode(5)
    h = ListNode(8)
    root.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    #h.next = b
    root.recurse()
    result = so.deleteDuplicates(root)
    print result.recurse()
    print root.recurse()
