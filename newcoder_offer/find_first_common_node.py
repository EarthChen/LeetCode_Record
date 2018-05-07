# 输入两个链表，找出它们的第一个公共结点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        list1 = []
        node1 = pHead1
        node2 = pHead2
        # 使用一个列表存储第一个链表的所有节点
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        # 循环遍历第二个链表判断是否存在列表中
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next
