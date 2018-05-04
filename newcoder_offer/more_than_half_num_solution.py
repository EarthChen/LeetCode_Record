# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 求的数组长度的一半
        mid = len(numbers) / 2
        # 遍历数组
        for i in numbers:
            # 判断数组中元素出现的次数
            if numbers.count(i) > mid:
                return i
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
