# Determine whether an integer is a palindrome. Do this without extra space.

# 不用额外的空间判断一个数字是否是回文


class Solution:
    def isPalindrome(self, x):
        # 将数字转换为字符串
        x = str(x)
        # 得到字符串的长度
        n = len(x)
        # 对字符串进行迭代
        for i in range(n):
            # 判断头和尾是否相等并且头要小于尾
            if x[i] != x[n - i - 1] and i < n - i - 1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    print(solution.isPalindrome(1000021))
