# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。


class Solution:
    def Convert(self, pRootOfTree):
        # 处理根节点为空
        if not pRootOfTree:
            return pRootOfTree
        # 只有根节点的情况
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while (left.right):
                left = left.right
            # 　交换节点的值
            pRootOfTree.left, left.right = left, pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while (right.left):
                right = right.left
            # 　交换节点的值
            pRootOfTree.right, right.left = right, pRootOfTree

        # 当左子树存在时
        while (pRootOfTree.left):
            # 左子树赋值给自己
            pRootOfTree = pRootOfTree.left
        # 返回链表的头节点
        return pRootOfTree
