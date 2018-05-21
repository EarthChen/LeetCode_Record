# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymBT(pRoot, pRoot)

    def isSymBT(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.isSymBT(tree1.left, tree2.right) and self.isSymBT(tree1.right, tree2.left)
