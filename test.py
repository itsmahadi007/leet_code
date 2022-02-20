# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solver(self, r1, r2):
        if r1 == None and r2 == None:
            return None
        if r1 and r2:
            root = TreeNode(r1.val + r2.val)
            root.left = self.solver(r1.left, r2.left)
            root.right = self.solver(r1.right, r2.right)
            return root
        elif r1 == None:
            return r2
        else:
            return r1

    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        return self.solver(root1, root2)


# in inorder
def inorder(node):
    if not node:
        return

    # first recur on left child
    inorder(node.left)

    # then print the data of node
    print(node.data, end=" ")

    # now recur on right child
    inorder(node.right)


def main():
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    s = Solution()
    root3 = s.mergeTrees(root1, root2)
    print("The Merged Binary Tree is:")
    inorder(root3)


main()
