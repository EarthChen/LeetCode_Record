# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
#
#
# 输出描述:
# 如果当前字符流没有存在出现一次的字符，返回#字符。


class Solution:
    # 返回对应char
    def __init__(self):
        """
        使用一个字符串和一个字典保存字符串出现的次数
        """
        self.s = ''
        self.dict1 = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            # 如果键值对的值为1(出现的次数为1)
            if self.dict1[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # 每次将字符串加上新字符
        self.s = self.s + char
        # 判断当前字符是否是字典中的键
        if char in self.dict1:
            # 将对应的键值+1
            self.dict1[char] = self.dict1[char] + 1
        else:
            # 不存在即直接赋值为1
            self.dict1[char] = 1
