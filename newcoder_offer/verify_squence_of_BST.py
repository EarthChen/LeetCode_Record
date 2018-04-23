# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同


class Solution:
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        # 数组的最后元素是该树的根节点
        root = sequence[-1]
        left = 0
        # 找到最后一个小于根节点的元素
        while sequence[left] < root:
            left += 1
        # 遍历最后一个小于根节点的元素到根节点之前
        for i in range(left, length - 1):
            # 判断是否大于根节点(右子树元素)
            if sequence[i] < root:
                return False
        # 递归左右子树
        return self.VerifySquenceOfBST(sequence[:left]) \
               or self.VerifySquenceOfBST(sequence[left:length - 1])
