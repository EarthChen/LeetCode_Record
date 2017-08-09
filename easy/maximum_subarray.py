# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# 计算列表中连续子数组的最大和

class Solution:
    def maxSubArray2(self, nums):
        """
        计算列表中连续子数组的最大和
        :param nums: list[int]
        :return: int
        """
        start = 0
        stop = 0
        length = len(nums)
        if length == 1:
            return sum(nums)
        largest_sum = nums[0]
        for i in range(0, length):
            max_sum = nums[0]
            for j in range(i, length):
                ij_sum = sum(nums[i: j + 1])
                if ij_sum > max_sum:
                    stop = j
                    max_sum = ij_sum
            if max_sum > largest_sum:
                start = i
                largest_sum = max_sum
        return largest_sum

    def maxSubArray(self, nums):
        """
        计算列表中连续子数组的最大和
        :param nums: list[int]
        :return: int
        """
        if not nums:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            # 计算当前的和与i相加之后的和比较的最大值
            cur_sum = max(i, cur_sum + i)
            # 计算当前和与最大和比较的最大值
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, -1]))
