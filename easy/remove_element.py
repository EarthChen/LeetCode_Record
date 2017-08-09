# Given an array and a value,
#  remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array,
#  you must do this in place with constant memory.
#
# The order of elements can be changed.
#  It doesn't matter what you leave beyond the new length.


class Solution:
    def removeElement(self, nums, val):
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length, nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
