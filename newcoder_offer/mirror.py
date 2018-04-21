#
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述:
# 二叉树的镜像定义：源二叉树
#     	    8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9 11
#     	镜像二叉树
#     	    8
#     	   /  \
#     	  10   6
#     	 / \  / \
#     	11 9 7  5

class Solution:
    def Mirror(self, root):
        """
        返回镜像树的根节点
        :param root:
        :return:
        """
        # 如果跟节点为空
        if not root:
            return None
        # 交换左子树和右子树
        root.left, root.right = root.right, root.left
        # 递归左右子树
        self.Mirror(root.left)
        self.Mirror(root.right)
