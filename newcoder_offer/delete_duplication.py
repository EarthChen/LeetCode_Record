# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        # 如果下一个节点不等于当前节点
        if head1.val != pHead.val:
            # 递归得到下一个节点
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            # 如果下一个节点等于当前节点并且下一个节点不为空
            while pHead.val == head1.val and head1.next is not None:
                # 使下一个节点为下下个节点
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead
