# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        result = []
        # 如果根节点为空
        if not root:
            return result
        # 将根节点放入列表中
        q = [root]
        # 当ｑ列表不为空
        while len(q):
            # 　将ｑ列表的第一个元素赋值给新节点
            node = q.pop(0)
            # 将节点的值添加到结果列表中
            result.append(node.val)
            # 如果节点有左子树
            if node.left:
                # 将节点的左子树放入ｑ列表
                q.append(node.left)
            if node.right:
                # 将节点的右子树放入ｑ列表
                q.append(node.right)
        return result
