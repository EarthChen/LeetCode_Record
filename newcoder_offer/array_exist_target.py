# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # array 二维列表
    def Find(self, target, array):
        col = 0
        # 行数
        row_n = len(array)
        # 列数
        col_n = len(array[0])
        # 判断是否大于最大值小于最小值
        if target > array[row_n - 1][col_n - 1] or target < array[0][0]:
            return False
        # 向上向右移动的时候不能越界
        while col <= col_n - 1 and row_n >= 0:
            # 需要和目标值比较的值(初始为左下角的元素或者是右上角)
            list_target = array[row_n - 1][col]
            # 如果目标值大于
            if target > list_target:
                # 向右移动
                col += 1
            # 如果等于返回true
            elif target == list_target:
                return True
            # 如果小于
            else:
                # 向上移动
                row_n -= 1
        return False


if __name__ == '__main__':
    list = [
        [1, 2, 3, 4],
        [1.2, 2.2, 3.2, 4.2],
        [1.3, 2.3, 3.3, 4.3]
    ]
    solution = Solution()
    print(solution.Find(2.4, list))
