# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

# 二进制加法

class Solution:
    def addBinary(self, a, b):
        """
        二进制加法
        :param a:
        :param b:
        :return:
        """
        a, b = int(a, 2), int(b, 2)
        return bin(a+b)[2:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('1101', '11'))
