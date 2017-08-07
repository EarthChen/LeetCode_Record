# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# 找出数组numbers中的两个数，它们的和为给定的一个数target，并返回这两个数的索引(不需要去重)
class Solution:
    def twoSum(self, nums, target):
        arr = {}  # 使用字典存储遍历过的num和对应下标{num:index}
        length = len(nums)  # 计算输入的列表长度
        for i in range(length):
            if (target - nums[i]) in arr:
                # 如果target-当前num的差在arr中，则表示已经找到答案，返回结果即可
                return [arr[target - nums[i]], i]
            # 否则，将该num及其下标存入arr中
            arr[nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))
