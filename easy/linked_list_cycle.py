# Given a linked list, determine if it has a cycle in it.

# 不使用额外的空间


class Solution:
    def hasCycle(self, head):
        """
        判断单链表中是否有环(不使用额外的空间)
        :param head: ListNode
        :return: bool
        """
        # 如果链表的头节点或者头节点的下一个节点为空
        if not head or not head.next:
            return False
        # 使用快慢指针
        # 慢指针一次向前移动一个节点
        slow = head
        # 快指针一次向前移动两个节点
        fast = head.next
        # 如果快指针存在并且快指针的下一个节点也存在
        while fast and fast.next:
            # 使慢指针向后移动一个节点
            slow = slow.next
            # 使快指针向后移动两个节点
            fast = fast.next.next
            # 如果快指针等于慢指针，即有环
            if slow == fast:
                return True
        return False
