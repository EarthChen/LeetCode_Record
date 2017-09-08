# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    def majorityElement(self, nums):
        """
        计算在数组中出现次数超过n/2次的元素
        :param nums:
        :return:
        """
        # for i in nums:
        #     if nums.count(i) > len(nums) / 2:
        #         return i
        # 假设目标元素为第一个
        major = nums[0]
        count = 1
        for i in range(len(nums)):
            # 能减到0就说明该元素不是最多的
            # 等于0为当前值第一次出现
            if count == 0:
                # 使其出现的次数变为1
                count += 1
                # 使目标值
                major = nums[i]
            # 迭代时等于目标元素，将出现的次数+1
            elif major == nums[i]:
                count += 1
            # 不等于时-1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([1, 2, 2, 2, 3]))
