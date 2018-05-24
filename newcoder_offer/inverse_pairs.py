# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出
# 。 即输出P%1000000007
# 输入描述:
# 题目保证输入的数组中没有的相同的数字
#
# 数据范围：
#
# 	对于%50的数据,size<=10^4
#
# 	对于%75的数据,size<=10^5
#
# 	对于%100的数据,size<=2*10^5


class Solution:
    def InversePairs(self, data):
        """
        先将原序列排序，然后从排完序的数组中取出最小的，
        它在原数组中的位置表示有多少比它大的数在它前面，
        每取出一个在原数组中删除该元素，保证后面取出的元素在原数组中是最小的，
        这样其位置才能表示有多少比它大的数在它前面，即逆序对数
        :param data:
        :return:
        """
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
