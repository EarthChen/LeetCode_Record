# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？


class Solution:
    def rectCover(self, number):
        """
        分析可知，还是斐波那契数列
        :param number:
        :return:
        """
        if number == 0:
            return 0
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.rectCover(6))
