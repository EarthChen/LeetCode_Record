# Implement int sqrt(int x).
#
# Compute and return the square root of x.


class Solution:
    def mySqrt2(self, x):
        """
        计算平方根
        :param x: int
        :return: int
        """
        import math
        return int(math.sqrt(x))

    def mySqrt(self, x):
        """
        计算平方根
        :param x: int
        :return: int
        """
        return int(x ** 0.5)


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))
