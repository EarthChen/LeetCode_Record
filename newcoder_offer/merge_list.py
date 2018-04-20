# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        """
        递归解决
        :param pHead1:
        :param pHead2:
        :return:
        """
        if not pHead1 or not pHead2:
            return pHead1 or pHead2
        # 比较pHead1和pHead2的值的大小
        if pHead1.val < pHead2.val:
            # 将pHead2递归到pHead1上
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            # 将pHead1递归到pHead2上
            pHead2.next = self.Merge(pHead2.next, pHead1)
            return pHead2
