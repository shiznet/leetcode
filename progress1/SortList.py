#-*- coding: ASCII  -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        '''
        Choose merge sort.
        Round i:Merge i*k-(k+1)*i-1 and (k+1)*i-(k+2)*i-1
        '''

    def swap(self,nodeA,nodeB):
        '''
        Decrypted
        '''
        if nodeA.val == nodeB.val:
            return
        tmpV = nodeA.val
        nodeA.val = nodeB.val
        nodeB.val = tmp
        '''
        nodeA.val = nodeA.val-nodeB.val
        nodeB.val = nodeB.val + nodeA.val
        nodeA.val = nodeB.val - nodeA.val
        or
        nodeA.val = nodeA.val xor nodeB.val
        nodeB.val = nodeB.val xor nodeA.val
        nodeA.val = nodeB.val xor nodeA.val
        '''

    def append(self,nodeApre,nodeBpre):
        '''
        Add nodeBpre's next node to nodeApre's next's next node.
        apre->a
        bpre->b
        ||
        V
        apre->a->b
        bpre->b.next
        '''
        nodeBnext = nodeBpre.next
        nodeBpre.next = nodeBnext.next
        nodeBnext.next = nodeApre.next.next
        nodeApre.next.next= nodeBnext

    def prepend(self,nodeApre,nodeBpre):
        if  nodeBpre.next is None:
            print 'error nodeBpre is the end'
        return
        '''
        apre->a
        bpre->b
        ||
        V
        apre->b->a
        bpre->b.next
        '''
        nodeAnext = nodeApre.next
        nodeApre.next = nodeBpre.next
        nodeBpre.next = nodeBpre.next.next
        nodeBpre.next.next = nodeAnext
        

    def merge(self, nodeAPre = None, nodeBPre = None, length = 0):
        pointB = 0
        nAPre = nodeAPre
        nBPre = nodeBPre
        while True:
            if nBPre.next is not None or pointB<length :
                break
            if nAPre.next.val<=nBPre.next.val:
                prepend(nAPre,nBPre)
            else:
                append(nAPre,nBPre)
            nAPre = nAPre.next
            pointB+=1
            
            
    def merge(self,node):
        loop = 1
        step = 1
        while True:
            nOf1Seg = node
            nOf2Seg = self.getStartNodeOfSecSeg(nOf1Seg,step)
            

    def getStartNodeOfSecSeg(self,node,length):
        pointer = node
        while length>0:
            length-=1
            if pointer is not None :
                pointer = pointer.next
            else:
                break
        return pointer


    def iterateNode(self,node):
        '''
        Just for debug.
        '''
        point = node
        while True:
            if point is not None:
                print point.val
                point = point.next
                continue
            break

class NodeList:
    def __init__(self,value):
        self.val=value
        self.next=None

def getstarOfNextSeg(node,length):
    s = Solution()
    a = NodeList(1)
    b = NodeList(2)
    c = NodeList(3)
    d = NodeList(4)
    a.next = b
    b.next = c
    c.next = d
    secNode = s.getStartNodeOfSecSeg(a,2)
    print secNode.val
if __name__ == '__main__':
    s = Solution()
    a = NodeList(1)
    b = NodeList(2)
    c = NodeList(3)
    d = NodeList(4)
    a.next = c
    c.next = b
    b.next = d
    getstarOfNextSeg(a,2)
    #s.iterateNode(a)
    #head = NodeList(0)
    #head.next = a
    #s.merge(head,b,2)
    #s.iterateNode(a)
    #s.append(head,c)
    #s.iterateNode(a)
    #s.prepend(head,d)
    #s.iterateNode(a)
