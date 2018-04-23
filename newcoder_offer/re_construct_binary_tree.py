# 输入某二叉树的前序遍历和中序遍历的结果，
# 请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        """
        根据前序和中序遍历重建二叉树
        :param pre:
        :param tin:
        :return:
        """
        if not pre and not tin:
            return None
        # 根据前序遍历获取到根节点
        root = TreeNode(pre[0])
        # 根据中序遍历得到根节点的索引
        i = tin.index(pre[0])
        # 　递归得到左子树（前序遍历的第１位到根节点索引＋１位，中序遍历的第０位到根节点的索引位）
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        # 　递归得到左子树（前序遍历的第根节点＋１位到最后一位，中序遍历的第根节点＋１到最后一位）
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root
