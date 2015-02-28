# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        osp = head
        tsp = head
        while True:
            if osp is None or tsp is None:
                return False
            osp = osp.next
            tsp = tsp.next
            if tsp is None:
                return False
            tsp = tsp.next
            if osp == tsp:
                return True

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

if __name__ == "__main__":
    a = ListNode("a")
    b = ListNode("a")
    c = ListNode("a")
    d = ListNode("a")
    e = ListNode("a")
    f = ListNode("a")
    g = ListNode("a")
    i = ListNode("a")
    j = ListNode("a")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = a
    f.next = g
    g.next = i
    i.next = j
    so = Solution()
    print so.hasCycle(None)
