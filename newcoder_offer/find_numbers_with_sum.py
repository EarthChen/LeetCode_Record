# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 使用一个字典存储乘积和两个数的键值对
        res = {}
        # 遍历列表
        for i in array:
            # 判断和减去该元素是否在该列表中
            if tsum - i in array:
                # 如果乘积的值不在字典中，将字典的值和键值对存储在字典中
                if i * (tsum - i) not in res.keys():
                    res[i * (tsum - i)] = (i, tsum - i)
        # 当字典不为空的时候，取出第一个元素的值即为最小的
        if res != {}:
            return list(sorted(res.items())[0][1])
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
