# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

import itertools


class Solution:
    def Permutation(self, ss):
        # 如果ss为空
        if not ss:
            return []
        # 使用标准库中的permutations进行全排序，使用map函数聚合
        # 使用set去重
        # 转为list并排序
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


if __name__ == '__main__':
    s = Solution()
    print(s.Permutation("abcb"))
