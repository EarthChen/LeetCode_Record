# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        # 直接向栈1压入元素
        self.stack1.append(node)

    def pop(self):
        # return xx
        # 如果栈2位空的情况
        if not self.stack2:
            # 迭代栈1，将栈1的元素弹出并压入栈2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            # 此时弹出栈2的元素
            return self.stack2.pop()
        # 如果栈1不为空，说明已经将元素压入栈2，直接弹出即可
        return self.stack2.pop()
