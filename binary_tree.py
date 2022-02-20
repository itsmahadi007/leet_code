# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree


# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


from typing import Optional


class TreeNode:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.data += root2.data
        root1.left = Solution.mergeTrees(root1.left, root2.left)
        root1.right = Solution.mergeTrees(root1.right, root1.right)
        return root1


# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)


# create root
# root = Node(1)
""" following is the tree after above statement
        1
      /   \
     None  None"""

# root.left = Node(2)
# root.right = Node(3)

""" 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None"""


# root.left.left = Node(4)
"""4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None"""
