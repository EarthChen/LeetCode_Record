# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# The input is assumed to be a 32-bit signed integer.
#  Your function should return 0 when the reversed integer overflows.

# 将数字倒置，并且输出结果需要在32位有符号数内


class Solution:
    def reverse(self, x):
        # 对x判断为正还是为负
        if x < 0:
            x = abs(x)
            # 先将数字转为字符串，再用反向切片操作(其他语言也都有字符串倒置函数)
            return self.isOverFlows(-int(str(x)[::-1]))
        else:
            return self.isOverFlows(int(str(x)[::-1]))

    # 判断x是否在32位有符号数
    def isOverFlows(self, x):
        if pow(-2, 31) < x < pow(2, 31):
            return x
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))
