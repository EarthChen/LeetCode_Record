# Given a sorted array,
# remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2,
#  with the first two elements of nums being 1 and 2 respectively.
#  It doesn't matter what you leave beyond the new length.
# 将数组去重求出长度


class Solution:
    def removeDuplicates(self, nums):
        '''
        :param nums: list[int]
        :return:int
        '''
        # 如果数组为空，则返回0
        if not nums:
            return 0
        new_length = 0
        length = len(nums)
        # 从1到n-1开始循环遍历
        for i in range(1, length):
            # 如果i不等于nums[now_length](其实是i-1)
            if nums[i] != nums[new_length]:
                new_length += 1
                nums[new_length] = nums[i]
        return new_length + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([]))
