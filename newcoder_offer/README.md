# 牛客网剑指offer

## 二维数据中的查找

### 题目描述

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

### 分析
本题关键在于找到左下角和右上角这两个元素，因为这两个元素在两个方向是分别递增和递减，就可以有规律的移动需要比较的目标元素。如果选用左上角或者右下角，对于两个方向都是递增或递减

```Python
class Solution:
    # array 二维列表
    def Find(self, target, array):
        col = 0
        # 行数
        row_n = len(array)
        # 列数
        col_n = len(array[0])
        # 判断是否大于最大值小于最小值
        if target > array[row_n - 1][col_n - 1] or target < array[0][0]:
            return False
        # 向上向右移动的时候不能越界
        while col <= col_n - 1 and row_n >= 0:
            # 需要和目标值比较的值(初始为左下角的元素或者是右上角)
            list_target = array[row_n - 1][col]
            # 如果目标值大于
            if target > list_target:
                # 向右移动
                col += 1
            # 如果等于返回true
            elif target == list_target:
                return True
            # 如果小于
            else:
                # 向上移动
                row_n -= 1
        return False
```

## 替换空格

### 题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

### 分析
看到题目的直接反应就是用字符串的替换方法，可能题目的意思时不能调用str的方法，但是牛客这里可以通过。

看有的解析还用了正则替换，当然都可以

```Python
class Solution:
# s 源字符串
    def replaceSpace(self, s):
        return str(s).replace(" ", "%20")
```


### 题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

### 分析
看到题目的直接反应就是用字符串的替换方法，可能题目的意思时不能调用str的方法，但是牛客这里可以通过。

看有的解析还用了正则替换，当然都可以

```Python
# s 源字符串
    def replaceSpace(self, s):
        return str(s).replace(" ", "%20")
```

## 从尾到头打印链表

### 题目描述
输入一个链表，从尾到头打印链表每个节点的值。

### 分析

有很多种办法，可以正向遍历存入列表，然后翻转列表；可以使用栈存储，还可以使用递归向列表中添加节点的值

```Python
class Solution:
    def __init__(self):
        self.list1 = []

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is not None:
            self.printListFromTailToHead(listNode.next)
            self.list1.append(listNode.val)
        return self.list1
```

## 斐波那契数列

### 题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39

### 分析
首先想到的是递归，最简洁，但是会有超时之类的问题，所以改为迭代相加


```Python
class Solution:
    def Fibonacci(self, n):
        """
        斐波那契数列
        :param n:
        :return:
        """
        num0 = 0
        num1 = 1
        num_n = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n + 1):
            num_n = num0 + num1
            num0 = num1
            num1 = num_n
        return num_n
```


## 跳台阶

### 题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

### 分析
通过分析前几次结果，我们也能发现这也是一个斐波那契数列，所以按照同样的方法即可
f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5，  可以总结出f(n) = f(n-1) + f(n-2)的规律

```Python
class Solution:
    def jumpFloor(self, number):
        """
        f(n) = f(n-1) + f(n-2)
        :param number:
        :return:
        """
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a
```

## 变态跳台阶

### 题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


### 分析
1. 第一种方法:
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)

2. 第二种方法
每个台阶都有跳与不跳两种情况（除了最后一个台阶），最后一个台阶必须跳。所以共用2^(n-1)中情况

```Python
class Solution:

    def jumpFloorII(self, number):
        """
        每个台阶都有跳与不跳两种情况（除了最后一个台阶），最后一个台阶必须跳。所以共用2^(n-1)中情况
        :param number: int
        :return: int
        """
        if number <= 0:
            return 0
        else:
            return pow(2, number - 1)
```

## 矩形覆盖

### 题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

### 分析
通过分析前几次结果，我们也能发现这也是一个斐波那契数列，所以按照同样的方法即可,
对于0这个特殊值需要特殊处理

```Python
class Solution:
    def rectCover(self, number):
        """
        分析可知，还是斐波那契数列
        :param number:
        :return:
        """
        if number == 0:
            return 0
        a, b = 1, 1
        for i in range(number):
            a, b = b, a + b
        return a
```

## 二进制中1的个数

### 题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？


### 分析
重点在怎么求补码，我的解法是转换为二进制字符串然后统计1的个数

还有吧一种使用&进行操作的这里不做说明

```Python
class Solution:
    def NumberOf1(self, n):
        """
        求补码然后使用字符串count函数统计
        :param n:
        :return:
        """
        if n < 0:
            return bin(2 ** 32 + n).count('1')
        return bin(n).count('1')
```

## 二进制中1的个数

### 题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

### 分析
没怎么研究，直接使用的内置函数，通过查阅资料，看到一种快速幂求解方式，有兴趣自己研究下

```Python
class Solution:

    def Power(self, base, exponent):
        """
        还可以使用快速幂求法
        :param base: 
        :param exponent: 
        :return: 
        """
        return pow(base, exponent)
```

## 调整数组顺序使奇数位于偶数前面

### 题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

### 分析
用了最简单的解法，创建两个列表分别接收奇数和偶数，最后拼起来

```Python
class Solution:
    def reOrderArray(self, array):
        odd_list = []
        even_list = []
        for i in array:
            if i % 2 != 0:
                odd_list.append(i)
            else:
                even_list.append(i)
        return odd_list + even_list
```

>注：
>- 上述测试在**Python3.5**中成功
>- 上述文字皆为个人看法，如有错误或建议请及时联系我


