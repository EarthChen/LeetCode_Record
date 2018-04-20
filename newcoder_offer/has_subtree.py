# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        # 如果root1或者root2有一个为null
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) \
               or self.HasSubtree(pRoot1.left, pRoot2) \
               or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, A, B):
        """
        判断是否时子树
        :param A:
        :param B:
        :return:
        """
        if not B:
            return True
        # 判断a不为空或者a的值与b的值不相等
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) \
               and self.is_subtree(A.right, B.right)
