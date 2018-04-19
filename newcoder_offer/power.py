# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。


class Solution:

    def Power(self, base, exponent):
        """
        还可以使用快速幂求法
        :param base:
        :param exponent:
        :return:
        """
        return pow(base, exponent)


if __name__ == '__main__':
    solution = Solution()
    print(solution.Power(2, -3))
