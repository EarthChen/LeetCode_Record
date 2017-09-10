# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


class Solution:
    def removeElements(self, head, val):
        """
        删除单链表中与给定值相等的元素
        :param head: ListNode
        :param val: int
        :return: ListNode
        """
        # 如果单链表为空
        if not head:
            return None
        p = head
        # p的下一个节点不为空
        while p.next is not None:
            # 判断下一个节点的值事多等于val
            if p.next.val == val:
                # 将下下个节点赋给下个节点
                p.next = p.next.next
            else:
                # 如果不等于，就把下一个节点赋给o
                p = p.next
        # 如果删除完节点此时头节点的值刚好等于目标值
        if head.val == val:
            return head.next
        return head
