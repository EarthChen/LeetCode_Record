# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
# 今天测试组开完会后,他又发话了:在古老的一维模式识别中,
# 常常需要计算连续子向量的最大和,当向量全为正数的时候,
# 问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
# 并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
# 连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住
# ？(子向量的长度至少是1)


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0:
            return []
        temp_sum = 0
        list_sum = []
        for i in array:
            # 将当前值累加
            temp_sum = temp_sum + i
            # 将当前的和放入列表中
            list_sum.append(temp_sum)
            # 如果当前和是大于0的，继续遍历
            if temp_sum > 0:
                continue
            # 否则将当前和赋值为0，避免负数影响
            else:
                temp_sum = 0
        # 得到和列表中的最大和值
        return max(list_sum)
