# Given an array of integers, every element appears twice except for one.
#  Find that single one.



class Solution:
    def singleNumber(self, nums):
        """
        找到数组只只出现了一次的元素(其他元素都出现了两次)
        :param nums: list[int]
        :return: int
        """
        # 使用set()去重把每个元素都得到一个
        # 求出所有单个元素的和,求出两倍的值
        # 再减去未去重时所有元素的和
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([1, 2, 2, 1, 4, 3, 3]))
