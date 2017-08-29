# Given a binary tree and a sum, determine
# if the tree has a root-to-leaf path such that adding up
# all the values along the path equals the given sum.


class Solution:
    def hasPathSum(self, root, sum):
        """
        判断从根到叶子节点的值之和是否有等于sum的
        :param root: TreeNode
        :param sum: int
        :return: bool
        """
        # 如果是空树
        if not root:
            return False
        # 如果只有根节点，并且根节点的值等于sum
        if root.val == sum and not root.left and not root.right:
            return True
        # 递归判断对左右节点的情况，每次需要将sum减去节点的值
        return self.hasPathSum(root.left, sum - root.val) \
               or self.hasPathSum(root.right, sum - root.val)
