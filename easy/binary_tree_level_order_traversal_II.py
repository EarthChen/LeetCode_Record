# Given a binary tree,
# return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]



class Solution:
    def levelOrderBottom(self, root):
        """
        返回节点值的自底向上的顺序遍历。（从左到右，从叶到根逐级地）
        :param root: TreeNode
        :return: list[list[int]]
        """
        stack = [(root, 0)]
        res = []
        # 如果栈不为空
        while stack:
            # 将栈中最后一个元素弹出
            node, level = stack.pop()
            # 如果该结点存在
            if node:
                # 如果结果列表的长度小于层数+1
                if len(res) < level + 1:
                    res.insert(0, [])
                # 将当前结点的值添加在结果列表中
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res
