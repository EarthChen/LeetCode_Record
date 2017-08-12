# Given a sorted linked list,
# delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
from data_structure.linked_list import LinkList
# 有序单链表去重

class Solution:
    def deleteDuplicates(self, head):
        """
        有序单链表去重
        :param head: ListNode
        :return: ListNode
        """
        current = head
        # 如果当前结点不为空
        while current:
            # 如果当前结点的下一个结点存在
            # 并且当前结点的值等于下一个结点的值
            while current.next and current.val == current.next.val:
                # 当前结点的下一个结点等于当前结点的下下个结点
                current.next = current.next.next
            # 再降当前结点的下一个结点赋值给当前结点
            current = current.next
        # 返回已经去重的单链表
        return head


if __name__ == '__main__':
    solution = Solution()
    link = LinkList()
    link.append(1)
    link.append(1)
    link.append(2)
    print(solution.deleteDuplicates(link._head))
    link.print()
