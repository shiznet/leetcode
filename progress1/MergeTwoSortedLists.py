# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        """
        Persume list is ascendent.
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            result = l1
            pointera = l1.next
            pointerb = l2
        else:
            result = l2
            pointera = l1
            pointerb = l2.next
        root = result
        while pointera is not None and pointerb is not None:
            if pointera.val > pointerb.val:
                result.next = pointerb
                pointerb = pointerb.next
            else:
                result.next = pointera
                pointera = pointera.next
            result = result.next
        if pointera is not None:
            result.next = pointera
        elif pointerb is not None:
            result.next = pointerb
        return root
        
def arrayToList(array):
    if array is None:
        return None
    root = ListNode(-1)
    pointer = root
    for v in array:
        pointer.next = ListNode(v)
        pointer = pointer.next
    return root.next

def recursive(list):
    pointer = list
    while pointer is not None:
        print pointer.val
        pointer = pointer.next

if __name__ == "__main__":
    so = Solution()
    a1 = [1,2,5,6,9]
    a2 = [3,4,7,8]
    l1 = arrayToList(a1)
    l2 = arrayToList(a2)
    result = so.mergeTwoLists(l1,l2)
    recursive(result)

