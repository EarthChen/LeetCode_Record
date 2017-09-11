# Reverse a singly linked list.




class Solution:
    def removeElements(self, head):
        """
        倒置单链表
        :param head: ListNode
        :return: ListNode
        """
        # 初始设前一个节点为空
        pre = None
        while head:
            # 将head赋值给当前节点
            current = head
            # 将head的下一个节点赋值给head节点
            head = head.next
            # 将前一个节点赋给当前节点的下一个节点
            current.next = pre
            # 将当前节点赋给前一个节点
            pre = current
        return pre
