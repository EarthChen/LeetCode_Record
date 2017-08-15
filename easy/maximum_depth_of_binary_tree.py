# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes
# along the longest path from the root node down to
#  the farthest leaf node.


class Solution:
    def maxDepth(self, root):
        """
        计算树的最大深度
        :param root: TreeNode
        :return: int
        """
        # 如果根结点为空返回0
        if not root:
            return 0
        # 计算左右子树的中的最大深度，加上根节点
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
