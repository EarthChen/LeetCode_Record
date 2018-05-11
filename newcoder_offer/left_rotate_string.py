# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
# 就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，
# 请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,
# 要求输出循环左移3位后的结果，即“XYZdefabc”


class Solution:
    def LeftRotateString(self, s, n):
        # 当n大于字符串长度或者小于0的时候，等于没有变
        if n >= len(s) or n <= 0:
            return s
        # 将字符串的前n位拼接到字符串的最后即可
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = Solution()
    print(s.LeftRotateString('abcXYZdef', 3))
