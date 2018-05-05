# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。


import itertools


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = map(str, numbers)
        # 全排列去重转列表排序取最小值
        res = sorted(list(set(map(''.join, itertools.permutations(numbers)))))
        return res[0]
