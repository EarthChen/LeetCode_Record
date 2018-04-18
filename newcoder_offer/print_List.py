# 输入一个链表，从尾到头打印链表每个节点的值。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def __init__(self):
        self.list1 = []

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is not None:
            self.printListFromTailToHead(listNode.next)
            self.list1.append(listNode.val)
        return self.list1
