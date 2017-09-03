# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

import copy


class Solution:
    def generate(self, numRows):
        # 最外侧的列表
        allrows = []
        # 每一行的列表
        row = []
        # 循环迭代每一行
        for i in range(numRows):
            # 像每行的第一个元素插入1
            row.insert(0, 1)
            # 对该行进行迭代(1开始因为已经插入了1，该行的长度-1因为保留了上一行的参数)
            for j in range(1, len(row) - 1):
                # 其中的参数等于索引为j和j+1位置的和
                row[j] = row[j] + row[j + 1]
            # 进行深拷贝，如果不进行深拷贝，Python会一直操作的是一个row最后只会append一个相同的row
            allrows.append(copy.deepcopy(row))
        return allrows


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
