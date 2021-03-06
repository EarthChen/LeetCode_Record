# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
#  In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.


class Solution:
    def climbStairs(self, n):
        """

        :param n: int
        :return: int
        """
        a = b = 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))
