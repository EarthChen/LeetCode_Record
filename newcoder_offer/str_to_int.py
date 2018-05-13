# 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
#  数值为0或者字符串不是一个合法的数值则返回0


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        number = 0
        start = 0
        flage = 1
        if s[0] == '+':
            start = 1
        elif s[0] == '-':
            flage = -1
            start = 1
        # 遍历字符串
        for i in range(start, len(s)):
            # 如果不在0到9
            if s[i] < '0' or s[i] > '9':
                return 0
            else:
                # 转换为数字
                number = number * 10 + flage * (ord(s[i]) - ord('0'))
        return number
