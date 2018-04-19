# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。


class Solution:
    def reOrderArray(self, array):
        """
        将奇数和偶数分别存列表中，最后拼起来
        :param array:
        :return:
        """
        odd_list = []
        even_list = []
        for i in array:
            if i % 2 != 0:
                odd_list.append(i)
            else:
                even_list.append(i)
        return odd_list + even_list


if __name__ == '__main__':
    solution = Solution()
    print(solution.reOrderArray([1, 2, 3, 4, 5, 6]))
