from XMLToNodeTree import NodeTreeBuilder
from TreeNode import TreeNode
# Definition for a  binary tree node
# class TreeNode:
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        self.compareResult = True
        self.traverser(p, q)
        return self.compareResult

    def traverser(self, p, q):
        if p is None or q is None:
            if q is not None or p is not None:
                self.compareResult = False
                return
            else:
                return
        if p.val != q.val:
            self.compareResult = False
            return
        self.traverser(p.left, q.left)
        if self.compareResult:
            self.traverser(p.right, q.right)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == "__main__":
    builder = NodeTreeBuilder()
    roota = builder.build("tc/single.xml")
    rootb = builder.build("tc/balancetree.xml")
    rootc = builder.build("tc/balancetree.xml")
    rootd = builder.build("tc/randomtree.xml")
    roote = builder.build("tc/randomtree.xml")
    so = Solution()
    print so.isSameTree(roota, rootb)
    print so.isSameTree(rootc, rootb)
    print so.isSameTree(rootc, roota)
    print so.isSameTree(rootc, rootd)
    print so.isSameTree(roote, rootd)
