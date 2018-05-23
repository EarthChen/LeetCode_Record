# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
# 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值


class Solution:
    x = []

    def Insert(self, num):
        # 将数字添加到列表中并排序
        self.x.append(num)
        self.x.sort()

    def GetMedian(self, x):
        # 得到长度
        n = len(self.x)
        # 判断奇数偶数
        if n % 2 == 1:
            return self.x[n // 2]
        else:
            return (self.x[n // 2 - 1] + self.x[n // 2]) / 2.0
