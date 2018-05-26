# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，、
# 每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
#  例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
# 因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


class Solution:
    def __init__(self):
        # 使用一个字典存储行列为键，值为1的键值对
        self.vis = {}

    def movingCount(self, threshold, rows, cols):
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        # 计算行坐标和列坐标的数位之和是否大于
        if row / 10 + row % 10 + col / 10 + col % 10 > threshold:
            return 0
        # 判断开始的行列是否大于总的行列
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        # 判断行列是否在字典中
        if (row, col) in self.vis:
            return 0
        # 将当前遍历的行列存入字典中
        self.vis[(row, col)] = 1
        # 将四个方向递归并且加上开始的第一个格子
        return 1 + self.moving(threshold, rows, cols, row - 1, col) \
               + self.moving(threshold, rows, cols, row + 1, col) \
               + self.moving(threshold, rows, cols, row, col - 1) \
               + self.moving(threshold, rows, cols, row, col + 1)
