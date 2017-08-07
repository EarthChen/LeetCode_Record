# Given a string containing just the characters
#  '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.
#
# The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# 判断括号是否成对出现
class Solution:
    def isValid(self, s):
        '''
        :param s: str
        :return: bool
        '''
        left_char = '({['
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # 初始化一个空列表作为栈
        stack = []
        # 循环遍历字符串
        for i in s:
            # 如果字符是左括号就入栈
            if i in left_char:
                stack.append(i)
            else:
                # 如果也想加上对其他字符串匹配
                # if i in mp.keys():
                    # 栈为空或者传入的右括号不等于栈尾的左括号，即不符合条件
                if not stack or mp[i] != stack.pop():
                    return False
        # 判断栈是否为空，为空即成立
        if not stack:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("{}"))
