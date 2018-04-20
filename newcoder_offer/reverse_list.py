# 输入一个链表，反转链表后，输出链表的所有元素。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        """
        倒置链表
        :param pHead:
        :return:
        """
        # 判断当前节点是否为空或者下一个节点为空
        if not pHead or not pHead.next:
            return pHead
        # 初始化未节点为空
        last = None
        # 循环迭代头节点
        while pHead:
            # 创建一个中间节点接受头节点的下一个节点
            tmp = pHead.next
            # 将尾节点赋值给尾节点
            pHead.next = last
            # 将头节点赋值给尾节点
            last = pHead
            # 将中间节点赋值给头节点
            pHead = tmp
        return last


if __name__ == '__main__':
    head = ListNode(12)
    for i in range(10):
        node = ListNode(i)
        head.next = node
        head = head.next

    solution = Solution()
    print(solution.ReverseList(head))
