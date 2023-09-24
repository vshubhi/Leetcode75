# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_leaf_nodes(root, leafs):
    if not root:
        return
    if not root.left and not root.right:
        leafs.append(root.val)
        return
    get_leaf_nodes(root.left, leafs)
    get_leaf_nodes(root.right, leafs)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1, leafs2 = [], []
        get_leaf_nodes(root1, leafs1)
        get_leaf_nodes(root2, leafs2)
        if len(leafs1) != len(leafs2):
            return False
        return all(leafs1[i]==leafs2[i] for i in range(len(leafs1)))

        