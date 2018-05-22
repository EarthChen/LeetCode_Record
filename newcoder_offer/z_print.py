# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        root = pRoot
        if not root:
            return []
        level = [root]
        # 使用一个列表保存结果
        result = []
        # 使用一个标识符标识左右遍历顺序
        left_to_right = False
        while level:
            # 保存当前节点值的列表
            cur_values = []
            # 保存下一层节点列表
            next_level = []
            # 　遍历层级节点
            for i in level:
                # 将当前遍历的节点值保存在当前节点值列表中
                cur_values.append(i.val)
                # 判断当前节点是否有左右子树，依次添加到下一层节点列表
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            # 　判断当前从左到右遍历还是从右到左遍历
            if left_to_right:
                cur_values.reverse()
            # 将遍历过节点值放入总结果列表中
            if cur_values:
                result.append(cur_values)
            # 将下一层节点付给当前层
            level = next_level
            # 将标识符倒置
            left_to_right = not left_to_right
        return result
