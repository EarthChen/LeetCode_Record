# 给定一颗二叉搜索树，请找出其中的第k大的结点。
# 例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k == 0:
            return None
        n = self.isorder(pRoot)
        if len(n) < k:
            return None
        else:
            # 返回第ｋ个节点
            return n[k - 1]

    def isorder(self, pRoot):
        re = []
        if not pRoot:
            return None
        if pRoot.left:
            # 如果左子树存在，递归得到所有子节点放入列表中
            re.extend(self.isorder(pRoot.left))
        # 将根节点放入列表中
        re.append(pRoot)
        if pRoot.right:
            # 如果右子树存在，递归得到所有子节点放入列表中
            re.extend(self.isorder(pRoot.right))
        return re
