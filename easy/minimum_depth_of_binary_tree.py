# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
#  from the root node down to the nearest leaf node

# 求树的最小深度


class Solution:
    def minDepth(self, root):
        # 如果是空树
        if not root:
            return 0
        # 递归求出子节点的深度
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 如果节点为空
        if left == 0 or right == 0:
            return left + right + 1
        # 不为空情况下计算左右子树的最小深度
        return min(left, right) + 1
