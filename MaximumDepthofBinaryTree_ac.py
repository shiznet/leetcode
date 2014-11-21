# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        self.maxDepth = 1
        self.traverse(root,1)
        return self.maxDepth

    def traverse(self,TreeNode,depth):
        if TreeNode.left is not None:
            self.traverse(TreeNode.left,depth+1)
        else:
            if depth>self.maxDepth:
                self.maxDepth = depth
        if TreeNode.right is not None:
            self.traverse(TreeNode.right,depth+1)
        else:
            if depth>self.maxDepth:
                self.maxDepth = depth


class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        super(TreeNode, self).__init__()
        self.val = x
        self.right = None
        self.left = None

na = TreeNode("a")
nb = TreeNode("b")
nc = TreeNode("c")
na.left = nb
na.right =nc
nd = TreeNode("d")
ne = TreeNode("e")
nf = TreeNode("f")
nc.right = nd
nd.left = ne
ne.left = nf
so = Solution()
print so.maxDepth(na)
