# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

# 判断一颗树是否是镜像的，


class Solution:
    def isSymmetric(self, root):
        """
        判断一颗树是否是镜像树
        :param root: TreeNode
        :return: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, tree_node1, tree_node2):
        """
        判断两棵树是否镜像
        :param tree_node1: TreeNode
        :param tree_node2: TreeNode
        :return: bool
        """
        # 如果两个叶子结点均为空
        if not tree_node1 and not tree_node2:
            return True
        # 如果只有一个叶子结点为空
        if not tree_node1 or not tree_node2:
            return False
        # 当前叶子结点的值相等，并且一颗树的左子树等于另一颗树的右子树
        return (tree_node1.val == tree_node2.val) \
               and self.isMirror(tree_node1.right, tree_node2.left) \
               and self.isMirror(tree_node1.left, tree_node2.right)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isSymmetric()
