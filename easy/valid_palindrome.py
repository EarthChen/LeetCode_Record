# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.


class Solution:
    def isPalindrome(self, s):
        """
        判断字符串是否是回文(只考虑字母和数字)
        :param s: str
        :return: bool
        """
        # 分别得到第一个和最后一个字符的索引
        i, r = 0, len(s) - 1
        # 判断回文只需要判断一半
        while i < r:
            # 当左边字符索引小鱼右边字符串并且
            # 左字符串属于字母和数字时
            while i < r and not s[i].isalnum():
                i += 1
            # 当左边字符索引小鱼右边字符串并且
            # 右字符串属于字母和数字时
            while i < r and not s[r].isalnum():
                r -= 1
            # 为了判断相等，均转换为小写去判断是否相等
            if s[i].lower() != s[r].lower():
                return False
            # 左字符向后移动一个
            i += 1
            # 右字符向前移动
            r -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome('A man, a plan, a canal: Panama'))
