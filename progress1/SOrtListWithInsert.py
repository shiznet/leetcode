# -*- coding: ASCII  -*-
# Definition for singly-linked list.
import pdb


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# a->b->c->d->e
# a->d->c->b->e
# tmp=b 0
#
#
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        candiNode = head
        counter = 1
        while candiNode.next is not None:
            #pdb.set_trace()
            curNode = candiNode
            candiNode = candiNode.next
            self.sortback(head, curNode, counter)
            counter += 1
        return head

    def swapNextNode(self, nodeA, nodeB):
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

    def sortback(self, head, node, distance):
        pointer = head
        while pointer is not None and distance > 0:
            #pdb.set_trace()
            if pointer.next.val >= node.next.val:
                self.swapNextNode(pointer, node)
                return
            pointer = pointer.next
            distance -= 1

    def prepend(self, nodeA, nodeB):
        node = ListNode(nodeA.val)
        node.next = nodeA.next
        nodeA.val = nodeB.val
        nodeA.next = node
        if nodeB.next is None:
            nodeB = None
        else:
            nodeB.val = nodeB.next.val
            nodeB.next = nodeB.next.next

    def append(self, nodeA, nodeB):
        node = ListNode(nodeB.val)
        node.next = nodeA.next
        nodeA.next = node
        if nodeB.next is None:
            #how to remove my self?
            nodeB = nodeB.next
        else:
            nodeB.val = nodeB.next.val
            nodeB.next = nodeB.next.next

    def sortback(self, head, node, counter):
        pointer = head
        pointerNode = node
        while counter > 0:
            if pointer.val > pointerNode.val:
                self.prepend(pointer, pointerNode)
                return
            pointer = pointer.next
            counter -= 1


    def iterateList(self, node):
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
    listA = createTest([4, 2, 2, 3, 4])
    s.prepend(listA,listA.next.next.next.next)
    # result = s.insertionSortList(listA)
    s.iterateList(listA)

