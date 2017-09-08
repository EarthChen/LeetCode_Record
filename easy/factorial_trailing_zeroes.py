# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.



class Solution(object):
    def trailingZeroes(self, n):
        """
        求阶乘n!后面0的个数
        :param n: int
        :return: int
        """
        # count = 0
        # n_sum = 1
        # for i in range(1, n + 1):
        #     n_sum *= i
        # while n_sum % 10 == 0:
        #     n_sum = n_sum // 10
        #     count += 1
        # return count
        # 出现0的只会是5的倍数
        res = 0
        while n:
            n //= 5
            res += n
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(100))
