# Merge two sorted linked lists and return it as a new list.
#  The new list should be made by splicing together the nodes of the first two lists.

from data_structure.linked_list import LinkList, ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        # 如果l1或l2有一个为空，则返回另一个
        if not l1 or not l2:
            return l1 or l2
        # 比较l1和l2的值的大小
        if l1.val < l2.val:
            # 将l2递归到l1上
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            # 将l1递归到l2上
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTwoLists(ListNode(1), ListNode(2)))
