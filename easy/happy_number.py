# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
#  replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
#  or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    def isHappy(self, n):
        """
        判断一个数是否为开心数
        :param n: int
        :return: bool
        """
        # 将n分别赋给两个参数
        x = n
        y = n
        # 当x大于0进入循环
        # 只有n大于1的时候才有可能平方和为1
        while x > 1:
            # 将x的平方和的结果赋给x
            x = self.cal(x)
            # 如果结果为1，那么该数是开心数
            if x == 1:
                return True
            # 使y的平方和的平方和赋值给y
            y = self.cal(self.cal(y))
            # 如果结果为1，那么该数是开心数
            if y == 1:
                return True
            # 这里也就是n与n的平方和相等，就会死循环，不可能开心数
            if x == y:
                return False
        # 对1单独处理
        if x == 1:
            return True
        # 其他情况为0
        return False

    # 计算当前n的平方和
    def cal(self, n):
        n2 = 0
        for i in str(n):
            n2 += int(i) ** 2
        return n2


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(0))
