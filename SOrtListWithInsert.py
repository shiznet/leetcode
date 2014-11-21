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
        candiNode = head.next
        counter = 1
        while candiNode is not None:
            #pdb.set_trace()
            curNode = candiNode

            if candiNode.next is None:
                self.sortback(head,candiNode,counter)
                candiNode = None
            else:
                candiNode = candiNode.next
                self.sortback(head, curNode, counter)

            # self.sortback(head,curNode,counter)

            counter = counter+1
        return head

    def prepend(self, nodeA, nodeB):
        node = ListNode(nodeA.val)
        node.next = nodeA.next
        nodeA.val = nodeB.val
        nodeA.next = node
        if nodeB.next is None:
            #Just reference
            nodeB = None
            print("none")
        else:
            nodeB.val = nodeB.next.val
            nodeB.next = nodeB.next.next


    def sortback(self, head, node, counter):
        pointer = head
        candidateNode = node
        if node.next is None:
            if pointer.val >node.val:
                self.prepend(pointer,node)
        else:
            while counter > 0:
                if pointer.val > candidateNode.val:
                    self.prepend(pointer, candidateNode)
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
    #s.prepend(listA,listA.next.next.next.next)
    result = s.insertionSortList(listA)
    s.iterateList(listA)

