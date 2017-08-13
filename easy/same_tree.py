# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and
# the nodes have the same value


class Solution:
    def isSameTree(self, p, q):
        """
        判断两个二叉树是否相同（值相同即相同）
        :param p: TreeNode
        :param q: TreeNode
        :return: bool
        """
        # 如果p和q都不为空
        if p and p:
            # 当前结点的值是否相等
            if p.val == q.val:
                # 判断当前结点的下一个左右结点是否相等
                return self.isSameTree(q.left, p.left) \
                       and self.isSameTree(q.right, p.right)
        # 如果p和q均为空
        if not p and not q:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isSameTree())
