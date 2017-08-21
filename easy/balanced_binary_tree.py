# Given a binary tree, determine if it is height-balanced.
#
# For this problem,
#  a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.


class Solution:
    def isBalanced(self, root):
        """
        判断一个树是否为平衡二叉树
        当check函数的发挥值不等于-1时返回true，等于-1是返回false
        :param root: TreeNode
        :return: bool
        """
        return self.check(root) != -1

    def check(self, root):
        """
        检查结点
        :param root: TreeNode
        :return: int
        """
        # 结点为空时
        if root is None:
            return 0
        # 递归得出左子树的返回值
        left = self.check(root.left)
        # 递归得出右子树的返回值
        right = self.check(root.right)
        # 如果左子树不为平衡树或者右子树不为平衡二叉树，
        # 左右子树想减的值大于1(-1-(-1))左右子树不为平衡树的情况
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        # left right分别等于0或1的情况
        return 1 + max(left, right)
