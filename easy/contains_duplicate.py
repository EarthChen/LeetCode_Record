# Given an array of integers,
# find if the array contains any duplicates.
#  Your function should return true if any value appears at least twice in the array,
#  and it should return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums):
        """
        判断给定数组中是否包含重复项
        :param nums: list[int]
        :return: bool
        """
        # 如果有重复元素去重之后长度与未去重不一样
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))
