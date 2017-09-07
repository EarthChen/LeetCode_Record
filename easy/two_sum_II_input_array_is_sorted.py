# Given an array of integers that is already sorted in ascending order,
#  find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2






class Solution:
    def twoSum(self, numbers, target):
        """
        计算整形列表中是否有两个值的和与目标值相等
        :param numbers: list[int]
        :param target: int
        :return: list[int]
        """
        # 使用一个字典存储已经遍历过的元素
        dic = {}
        # 循环遍历
        for i in range(len(numbers)):
            # 如果目标值减去遍历的元素的值在字典中
            if target - numbers[i] in dic:
                # 即返回保存在字典中元素的下标
                # 并且要求索引从1开始 所以需要+1
                return [dic[target - numbers[i]] + 1, i + 1]
            # 将遍历过的值和下标存入字典中
            dic[numbers[i]] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15],9))
