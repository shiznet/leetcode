# Definition for a  binary tree node
from BinaryTreeInorderTraversal import Solution as recuso
from BinaryTreePreorderTraversal import Solution as preso
from TreeNode import TreeNode
import time

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num is None or len(num) == 0:
            return None
        self.num = num
        middle = (0+len(self.num)-1)>>1
        rootNode = TreeNode(num[middle])
        self.buildBST(rootNode, 0, middle - 1, 0)
        self.buildBST(rootNode, middle+1, len(self.num)-1, 1)
        return rootNode

    def buildBST(self, node, start, end, position):
        if start == end:
            self.createChild(node, start, position)
        elif end - start >= 1:
            middle = (start + end) >>1
            newnode = self.createChild(node, middle, position)
            self.buildBST(newnode, start, middle - 1, 0)
            self.buildBST(newnode, middle + 1, end, 1)

    def createChild(self, node, start, position):
        if position == 0:
            left = TreeNode(self.num[start])
            node.left = left
            return node.left
        elif position == 1:
            right = TreeNode(self.num[start])
            node.right = right
            return node.right


if __name__ == "__main__":
    so = Solution()
    rc = recuso()
    pre = preso()
    for i in range(32):
        list = range(i)
        print time.time()
        node = so.sortedArrayToBST(list)
        print time.time()
        result = rc.inorderTraversal(node)
        print "%d %d %d" % (i,len(list),len(result))

