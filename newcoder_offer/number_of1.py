# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


class Solution:
    def NumberOf1(self, n):
        """
        求补码然后使用字符串count函数统计
        :param n:
        :return:
        """
        if n < 0:
            return bin(2 ** 32 + n).count('1')
        return bin(n).count('1')


if __name__ == '__main__':
    solution = Solution()
    print(solution.NumberOf1(-6))
