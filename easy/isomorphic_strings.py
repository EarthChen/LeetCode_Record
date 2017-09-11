# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
#  No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.


class Solution:
    def isIsomorphic(self, s, t):
        """
        判断两个字符串是否是同构的
        :param s: str
        :param t: str
        :return: bool
        """
        # 根据同构定义迭代字符串找出字符串的结构
        # 根据索引得到结构
        return [s.find(i) for i in s] == [t.find(i) for i in t]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("foo", "bar"))
