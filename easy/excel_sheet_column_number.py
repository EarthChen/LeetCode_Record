# Given a column title as appear in an Excel sheet,
#  return its corresponding column number.
#
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution(object):
    def titleToNumber(self, s):
        """
        将excel中的列名转换为列序号
        :param s: str
        :return: int
        """
        # 设初始总和为0
        sum1 = 0
        # 指数初始为0
        k = 0
        # 将字符串倒叙迭代
        for i in s[::-1]:
            # 得到迭代的元素的数字
            i = ord(i) - 64
            # 得到该字符代表的数字
            sum1 += i * 26 ** k
            # 将指数+1
            k += 1
        return sum1


if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('AZ'))
