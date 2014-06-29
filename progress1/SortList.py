
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
        

    def merge(self, nodeAPre, nodeBPre, length):
        pointB = 0
        nAPre = nodeApre
        nBPre = nodeBpre
        while True:
            if nBpre.next is not None | pointB<length :
                break
            if nApre.next.val<=nBpre.next.val:
                prepend(nApre,nBpre)
            else:
                append(nApre,nBpre)
            nApre = nApre.next
            pointB+=1
            
            
    def iterateNode(self,node):
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

if __name__ == '__main__':
    s = Solution()
    a = NodeList(1)
    b = NodeList(2)
    c = NodeList(3)
    d = NodeList(4)
    a.next = c
    c.next = b
    b.next = d
    s.iterateNode(a)
    head = NodeList(0)
    head.next = a
    s.merge(head,b,2)
    s.iterateNode(a)
    #s.append(head,c)
    #s.iterateNode(a)
    #s.prepend(head,d)
    #s.iterateNode(a)
