# Given a positive integer,
#  return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#


class Solution:
    def convertToTitle(self, n):
        """
        将数字转换为excel的列名
        :param n: int
        :return: str
        """
        # 存放结果的字符串
        res = ''
        # n不为0时进入循环
        while n != 0:
            # 求余得到一个字符
            ch = chr((n - 1) % 26 + 65)
            # 除以26求模
            n = (n - 1) // 26
            res = ch + res
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(53))
