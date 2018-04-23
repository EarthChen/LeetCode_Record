# 输入两个整数序列，第一个序列表示栈的压入顺序，
# 请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False
        # 创建一个辅助栈
        stack = []
        for i in pushV:
            # 将遍历入栈顺序，添加到辅助栈中
            stack.append(i)
            # 如果栈不为空，且栈顶元素等于弹出序列
            while len(stack) and stack[-1] == popV[0]:
                # 出栈
                stack.pop()
                popV.pop(0)
        # 如果辅助栈为空
        if len(stack):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
