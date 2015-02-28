from XMLToNodeTree import NodeTreeBuilder as builder
# Definition for a  binary tree node
# class TreeNode:
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = []
        pointer = root
        while True:
            if pointer is not None:
                result.append(pointer.val)
                stack.append(pointer)
                pointer = pointer.left
            else:
                if len(stack) >0:
                    pointer = stack.pop()
                    pointer = pointer.right
                else:
                    break
        return result


if __name__ == "__main__":
    so = Solution()
    b = builder()
    random = b.build("tc/single.xml")
    print random
    array = so.preorderTraversal(None)
    print array

