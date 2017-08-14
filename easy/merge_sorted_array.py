# Given two sorted integer arrays nums1 and nums2,
#  merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space
#  (size that is greater or equal to m + n) to hold additional elements from nums2.
#  The number of elements initialized in nums1 and nums2 are m and n respectively.


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        将列表nums2合并到nums1上
        :param nums1: list[int]
        :param m: int
        :param nums2: list[int]
        :param n: int
        :return: void
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m - n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)
