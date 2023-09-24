# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class GoodBadNode:
    def __init__(self, val=0, good=False):
        self.val = val
        self.good = good


class Solution:
    count = 0
    @staticmethod
    def count_good_nodes(node, path):

        if not node:
            return
        # print(node.val)
        # for x in path:
        #     print(x.val, x.good, end=" ")
        # print()
        is_good = False
        if not path:
            is_good = True
            Solution.count+=1
        else:
            for i in range(len(path)-1, -1, -1):
                if path[i].val>node.val:
                    break
                elif path[i].val<=node.val and path[i].good:
                    Solution.count+=1
                    is_good = True
                    break
        path_node = GoodBadNode(node.val, is_good)
        path.append(path_node)
        Solution.count_good_nodes(node.left, path)
        Solution.count_good_nodes(node.right, path)
        path.pop()

    @staticmethod
    def count_good_nodes_opt(node, maxi):
        if node == None:
            return 0

        count = 1 if node.val>=maxi else 0
        count += Solution.count_good_nodes_opt(node.left, max(maxi, node.val))
        count += Solution.count_good_nodes_opt(node.right, max(maxi, node.val))
        return count

    def goodNodes(self, root: TreeNode) -> int:
        # Solution.count = 0
        # path = []
        # Solution.count_good_nodes(root, path)
        return Solution.count_good_nodes_opt(root, root.val)
        