# 统计一个数字在排序数组中出现的次数。

class Solution:
    def GetNumberOfK(self, data, k):
        """
        在Python中可以直接使用data.count(k)来解决

        为了题目的意义，这里使用二分查找
        :param data:
        :param k:
        :return:
        """
        length = len(data)
        if length == 0:
            return 0
        first = self.get_first_k(data, k, 0, length - 1)
        end = self.get_last_k(data, k, 0, length - 1)
        if first != -1 and end != -1:
            return end - first + 1
        return 0

    def get_first_k(self, data, k, start, end):
        """
        递归写法二分查找
        :param data:
        :param k:
        :param start:
        :param end:
        :return:
        """
        if start > end:
            return -1
        mid = start + (end - start) / 2
        if data[mid] > k:
            return self.get_first_k(data, k, start, mid - 1)
        elif data[mid] < k:
            return self.get_first_k(data, k, mid + 1, end)
        elif mid - 1 >= 0 and data[mid - 1] == k:
            return self.get_first_k(data, k, start, mid - 1)
        else:
            return mid

    def get_last_k(self, data, k, start, end):
        """
        循环写法二分查找
        :param data:
        :param k:
        :param start:
        :param end:
        :return:
        """
        length = len(data)
        mid = start + (end - start) / 2
        while start <= end:
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            elif mid + 1 < length and data[mid + 1] == k:
                start = mid + 1
            else:
                return mid
            mid = start + (end - start) / 2
        return -1
