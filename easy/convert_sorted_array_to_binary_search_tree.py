# Given an array where elements are sorted in ascending order,
#  convert it to a height balanced BST.
from data_structure.binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, num):
        """
        将已排序的数组转换为高度平衡二叉树
        :param num: list[int]
        :return: TreeNode
        """
        # 如果列表为空
        if not num:
            return None
        # 列表中间的值为列表长度整数2
        mid = len(num) // 2
        # root结点为以列表中间值为结点的值的结点
        root = TreeNode(num[mid])
        # 递归求出
        # 左子树为小于中间值一部分
        root.left = self.sortedArrayToBST(num[:mid])
        # 右子树为大于中间值的一部分
        root.right = self.sortedArrayToBST(num[mid + 1:])
        return root
