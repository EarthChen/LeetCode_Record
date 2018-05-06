# 把只包含因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含因子7。
#  习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return index
        # 使用一个列表保存丑数
        res = [1]
        i = 0
        j = 0
        k = 0
        # 当丑数数量不等于index时
        while len(res) != index:
            # 求出当前丑数*2 *3 *5中的最小值
            minV = min(res[i] * 2, res[j] * 3, res[k] * 5)
            # 将最小值放入丑数列表
            res.append(minV)
            # 判断当前丑数*2 *3 *5是否小于等于丑数
            if res[i] * 2 <= minV:
                i += 1
            if res[j] * 3 <= minV:
                j += 1
            if res[k] * 5 <= minV:
                k += 1
        # 返回最后一个丑数
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(5))
