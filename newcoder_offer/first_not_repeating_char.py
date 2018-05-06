# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)
# 中找到第一个只出现一次的字符,并返回它的位置


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == '':
            return -1
        for i in range(len(s)):
            # 当从前往后查找和从后向前查找时返回值相等时，即只出现了一次
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.FirstNotRepeatingChar('aaaaaaabv'))
