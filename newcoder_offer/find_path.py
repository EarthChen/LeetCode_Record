# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 如果是个空树
        if not root:
            return []
        # 如果根节点不为空，并且根节点的值等于指定值而且左右子树均为空
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        # 递归左子树
        left = self.FindPath(root.left, expectNumber - root.val)
        # 递归右子树
        right = self.FindPath(root.right, expectNumber - root.val)
        # 遍历拼接左右子树的结果
        for i in left + right:
            # 将根节点的值+i添加到res数组上
            res.append([root.val] + i)
        return res
