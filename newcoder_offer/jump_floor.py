# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


class Solution:
    def jumpFloor(self, number):
        """
        f(n) = f(n-1) + f(n-2)
        :param number:
        :return:
        """
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloor(6))
