# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def countPathTargetSum(self, root, target_sum, currPathSum, hm):
        if not root:
            return
        # print(root.val, currPathSum )
        currPathSum+=root.val
        oldPathSum = currPathSum - target_sum
        # print(root.val, oldPathSum, hm, hm.get(oldPathSum, 0), hm.get(currPathSum, 0))
        self.res += hm.get(oldPathSum, 0)
        hm[currPathSum] = hm.get(currPathSum, 0) + 1
        # print(root.val, currPathSum, oldPathSum, hm.get(oldPathSum, 0))
        self.countPathTargetSum(root.left, target_sum, currPathSum, hm)
        self.countPathTargetSum(root.right, target_sum, currPathSum, hm)
        hm[currPathSum] -= 1
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hm = {0:1}
        self.res = 0
        self.countPathTargetSum(root, targetSum, 0, hm)
        return self.res