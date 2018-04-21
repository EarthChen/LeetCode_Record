# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。


class Solution:

    def __init__(self):
        self.stack = []

    def push(self, node):
        """
        推入元素
        使当前元素的值作为键，当前最小值作为值
        :param node:
        :return:
        """
        curMin = self.min()
        if curMin is None or node < curMin:
            curMin = node
        self.stack.append((node, curMin))

    def pop(self):
        self.stack.pop()

    def top(self):
        """
        弹出顶部元素的值
        :return:
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][0]

    def min(self):
        """
        得到最小栈中最小的元素
        :return:
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][1]
