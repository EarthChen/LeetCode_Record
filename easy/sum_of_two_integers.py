# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
# Credits:
# Special thanks to @fujiaozhu for adding this problem and creating all test cases

# 不用加减号计算两个数之和


class Solution:
    def getSum(self, a, b):
        """
        不用加减法计算两个数之和
        :param a:
        :param b:
        :return:
        """
        while b:
            sum = a ^ b
            carry = (a & b) << 1
            a, b = sum, carry
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSum(4, 6))
