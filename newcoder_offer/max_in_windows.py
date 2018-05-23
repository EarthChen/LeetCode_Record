# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
#  针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
# {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
#  {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


class Solution:
    def maxInWindows(self, num, size):
        if size == 0 or size > len(num):
            return []
        max_num = []
        for i in range(len(num) - size + 1):
            max_num.append(max(num[i:i + size]))
        return max_num


if __name__ == '__main__':
    s = Solution()
    print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))
