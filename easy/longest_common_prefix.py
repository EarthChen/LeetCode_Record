# Write a function to find the longest common prefix string amongst an array of strings.

# 求出一个字符串数组中所有字符串的最长共同前缀
class Solution:
    def longestCommonPrefix(self, strs):
        # 判断字符串列表是否为空
        if not strs:
            return ''
        # 计算字符串列表中最短的字符串
        min_str = min(strs)
        # 计算最短字符串的长度
        min_length = len(min_str)
        # 初始令最长共同前缀字符串为最短字符串的第一个字符
        max_common_str = min_str[:1]
        for i in range(min_length):
            for str in strs:
                # 判断字符串列表中每个字符串的前i+1位是否与最长共同字符串相同
                # 不同则判断当前字符串是否为第1个，是则返回空，不是则返回前i位字符串
                if str[:i + 1] != max_common_str:
                    if i == 0:
                        return ''
                    return str[:i]
            # 当每个字符串前i+1位都与共同前缀字符相同时，判断字符串是否最短字符串相同
            # 相同则返回最长共同前缀字符
            if min_str == max_common_str:
                return max_common_str
            # 不相同则返回前i+1+1位字符串(使字符串向后移动一位)
            max_common_str = min_str[:i + 1 + 1]
        return max_common_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(['aa']))
