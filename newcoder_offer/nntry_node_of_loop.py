# 一个链表中包含环，请找出该链表的环的入口结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        if not pHead or not pHead.next:
            return None
        node = pHead
        while node:
            if node in tempList:
                return node
            else:
                tempList.append(node)
            node = node.next
