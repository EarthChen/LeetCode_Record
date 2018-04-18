# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


class Solution:

    def jumpFloorII(self, number):
        """
        每个台阶都有跳与不跳两种情况（除了最后一个台阶），最后一个台阶必须跳。所以共用2^(n-1)中情况
        :param number: int
        :return: int
        """
        if number <= 0:
            return 0
        else:
            return pow(2, number - 1)
