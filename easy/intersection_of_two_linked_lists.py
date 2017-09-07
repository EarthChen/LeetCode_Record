# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        求出两个单链表的交点
        :param headA: ListNode
        :param headB: ListNode
        :return: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        # 如果pa节点不等于pb节点
        while pa is not pb:
            # Python中的三元表达式格式为:为真时的结果 if 判定条件 else 为假时的结果
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa
