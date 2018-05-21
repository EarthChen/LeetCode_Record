# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return pNode
        # 如果有右子树，则找右子树的最左节点
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        # 没右子树，则找第一个当前节点是父节点左孩子的节点
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        # 退到了根节点仍没找到，则返回null
        return None
