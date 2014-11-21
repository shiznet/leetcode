# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        startNode = root 
        parentNode = root
        childNode = root.left
        while startNode.left is not None:
            parentNode = startNode
            startNode = startNode.left
            childNode = parentNode.left
            childNode.next = parentNode.right
            childNode = childNode.next
            parentNode = parentNode.next
            while parentNode is not None:
                childNode.next = parentNode.left
                childNode = childNode.next
                childNode.next = parentNode.right
                childNode = childNode.next
                parentNode = parentNode.next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

if __name__ == "__main__":
    so = Solution()
    a = TreeNode("a")    
    b = TreeNode("b")    
    c = TreeNode("c")    
    d = TreeNode("d")    
    e = TreeNode("e")    
    f = TreeNode("f")    
    g = TreeNode("g")    
    h = TreeNode("h")    
    i = TreeNode("i")
    j = TreeNode("j")
    k = TreeNode("k")
    l = TreeNode("l")
    m = TreeNode("m")
    n = TreeNode("n")
    o = TreeNode("o")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    d.right = i
    e.left = j
    e.right = k
    f.left = l
    f.right = m
    g.left = n
    g.right = o
    so.connect(a)
    print "end"
