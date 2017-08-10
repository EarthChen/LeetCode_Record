# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.

# 第n次的结果是对n-1次结果的解释


class Solution:
    def countAndSay(self, n):
        """

        :param n: int
        :return: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        # 得到上一次的结果
        n1_str = self.countAndSay(n - 1)
        # 末尾字符赋值为上一次结果的第一个字符
        last = n1_str[0]
        cnt = 1
        n_str = ''
        # 从索引1开始迭代
        for i in range(1, len(n1_str)):
            # 如果当前元素等于初始末尾字符(上一次结果的第一个字符)
            if n1_str[i] == last:
                cnt += 1
            else:
                n_str = n_str + str(cnt)
                n_str = n_str + last
                # 将数量重置为1
                cnt = 1
                last = n1_str[i]
        n_str = n_str + str(cnt)
        n_str = n_str + last
        return n_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(6))
