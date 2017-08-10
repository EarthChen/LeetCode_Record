# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.


class Solution:
    def lengthOfLastWord(self, s):
        """
        返回字符串中最后一个单词的长度
        :param s: str
        :return: int
        """
        # 先去掉首尾的空格
        # 在按空格切割字符串转换为列表
        # 取列表最后一个元素计算长度
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("   "))
