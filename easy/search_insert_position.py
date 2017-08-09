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
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 0))
