# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        root = pRoot
        level = [root]
        while level:
            cur_value = []
            next_level = []
            for i in level:
                cur_value.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if cur_value:
                result.append(cur_value)
            level = next_level
        return result
