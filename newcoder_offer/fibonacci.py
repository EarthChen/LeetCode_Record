# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39


class Solution:
    def Fibonacci(self, n):
        """
        斐波那契数列数列
        :param n:
        :return:
        """
        num0 = 0
        num1 = 1
        num_n = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n + 1):
            num_n = num0 + num1
            num0 = num1
            num1 = num_n
        return num_n


if __name__ == '__main__':
    solution = Solution()
    print(solution.Fibonacci(6))
