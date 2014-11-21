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
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = []
        pointer = root
        """
        is none: no
        has left:   yes push to stack
                    no add to result.has right:
                                                yes push to stack
                                                no
                 yes pop add to result.has right
        """
        while True:
            if pointer is None:
                if len(stack) == 0:
                    break
                pointer = stack.pop()
                result.append(pointer.val)
                if pointer.right is not None:
                    pointer = pointer.right
                else:
                    pointer = None
            else:
                stack.append(pointer)
                pointer = pointer.left
        return result


if __name__ == "__main__":
    so = Solution()
    b = builder()
    node = b.build("tc/randomtree.xml")
    print so.inorderTraversal(node)
    print so.inorderTraversal(None)
