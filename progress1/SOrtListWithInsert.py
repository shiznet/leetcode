#-*- coding: ASCII  -*-
# Definition for singly-linked list.
import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#a->b->c->d->e
#a->d->c->b->e
#tmp=b 0
#
#
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        tmpHead = ListNode(-1)
        tmpHead.next = head
        header = tmpHead
        candiNode = tmpHead.next
        while candiNode.next is not None:
            #pdb.set_trace()
            curNode = candiNode
            candiNode = candiNode.next
            self.sortback(header,curNode)
        return tmpHead.next

    def swapNextNode(self,nodeA,nodeB):
        '''
        a-b-c-d-e
        append a with c.next Node
        '''
        if nodeB is None:
            return
        #pdb.set_trace()
        tmpNode = ListNode(-1)
        tmpNode.next = nodeA.next
        nodeA.next = nodeB.next
        nodeB.next = nodeB.next.next
        nodeA.next.next = tmpNode.next

    def sortback(self,head,node):
        pointer = head
        while pointer is not None:
            #pdb.set_trace()
            if pointer.next.val >= node.next.val:
                self.swapNextNode(pointer,node)
                return
            if pointer.next.val == node.next.val:
                return
            pointer = pointer.next

    def iterateList(self,node):
        while node is not None:
            print node.val
            node = node.next

def createTest(array):
    head = ListNode(-1)
    cur = head
    for a in array:
        node = ListNode(a)
        cur.next = node
        cur = node
    return head.next
if __name__ == "__main__":
    s = Solution()
    listA = createTest([4,2, 2,3,4])
    result = s.insertionSortList(listA)
    s.iterateList(result)

