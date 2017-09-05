# Design a stack that supports push, pop, top,
#  and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        """
        向栈种推入一个元素
        :param x: int
        :return: void
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        """
        弹出一个元素
        :return: void
        """
        self.q.pop()

    def top(self):
        """
        得到栈顶元素
        :return: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self):
        """
        得到最小栈中最小的元素
        :return: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]
