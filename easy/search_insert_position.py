# Given a sorted array and a target value,
#  return the index if the target is found.
#  If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:
    def searchInsert(self, nums, target):
        # 判断是否在列表中
        if target in nums:
            # 存在即返回索引
            return nums.index(target)
        else:
            for i in range(len(nums)):
                # 当第一次大于目标值时就返回当前索引
                if nums[i] > target:
                    return i
            # 如果列表中灭有大于目标值的返回列表的长度
            return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 0))
