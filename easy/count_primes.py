# Count the number of prime numbers less than a non-negative number, n.



class Solution(object):
    def countPrimes(self, n):
        """
        计算小于非复数的素数n
        :param n: int
        :return: int
        """
        # 如果小于3，那么只有0符合要求
        if n < 3:
            return 0
        # 使用true和false来标志
        primes = [True] * n
        # 使列表前两个元素为false
        primes[0] = primes[1] = False
        # 计算素数只需要计算一半即可
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i:n:i] = [False] * len(primes[i * i:n:i])
        return sum(primes)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(9))
