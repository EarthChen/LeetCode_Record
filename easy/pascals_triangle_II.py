# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution:
    def getRow(self, rowIndex):
        """
        计算帕斯卡三角形的制定行数的元素
        :param rowIndex: int
        :return: list
        """
        row = [1]
        for i in range(rowIndex):
            # 使用列表推导式迭代x+y的值
            # 其中x和y分别等于[0] + row和row + [0]的第一列和第二列
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))
