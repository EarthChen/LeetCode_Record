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

## 数值的整数次方

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

## 反转链表

### 题目描述
输入一个链表，反转链表后，输出链表的所有元素。

### 分析
首先判断头节点或者第一个节点是否为空，在不为空的时候迭代链表

```Python
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        """
        倒置链表
        :param pHead:
        :return:
        """
        # 判断当前节点是否为空或者下一个节点为空
        if not pHead or not pHead.next:
            return pHead
        # 初始化未节点为空
        last = None
        # 循环迭代头节点
        while pHead:
            # 创建一个中间节点接受头节点的下一个节点
            tmp = pHead.next
            # 将尾节点赋值给尾节点
            pHead.next = last
            # 将头节点赋值给尾节点
            last = pHead
            # 将中间节点赋值给头节点
            pHead = tmp
        return last
```

## 合并两个排序的链表

### 题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则

### 分析
我们使用其中的一个结点将两个链表拼接起来，换句话说，就是将一个链表合并到另一个链表上，所以并不能创建一个新链表去进行操作。

当其中某一个链表为空时，只需要返回另一个链表即可，这种情况需要单独讨论

当两个链表均不为空时，我们需要去比较结点两个链表中结点的大小，当l1的结点值小于l2的结点时，我们就需要将l2合并到l1上，把l2的结点一个一个拼到l1上，知道l2为为空时，循环就可以结束了。这个过程是重复的，所以我们这里可以使用递归操作，反之，当l2的结点小于l1时，就把l1拼接到l2上


```Python
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        """
        倒置链表
        :param pHead:
        :return:
        """
        # 判断当前节点是否为空或者下一个节点为空
        if not pHead or not pHead.next:
            return pHead
        # 初始化未节点为空
        last = None
        # 循环迭代头节点
        while pHead:
            # 创建一个中间节点接受头节点的下一个节点
            tmp = pHead.next
            # 将尾节点赋值给尾节点
            pHead.next = last
            # 将头节点赋值给尾节点
            last = pHead
            # 将中间节点赋值给头节点
            pHead = tmp
        return last
```

## 树的子结构

### 题目描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

### 分析
判断是否是子树，也就是其中部分树与另一个树相等，我们可以单独写一个函数判断两个树是否相同，然后将一个树的左右子树递归带入即可

```Python
class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        # 如果root1或者root2有一个为null
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) \
               or self.HasSubtree(pRoot1.left, pRoot2) \
               or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, A, B):
        """
        判断是否时子树
        :param A:
        :param B:
        :return:
        """
        if not B:
            return True
        # 判断a不为空或者a的值与b的值不相等
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) \
               and self.is_subtree(A.right, B.right)
```

## 合并两个排序的链表

### 题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则

### 分析
我们使用其中的一个结点将两个链表拼接起来，换句话说，就是将一个链表合并到另一个链表上，所以并不能创建一个新链表去进行操作。

当其中某一个链表为空时，只需要返回另一个链表即可，这种情况需要单独讨论

当两个链表均不为空时，我们需要去比较结点两个链表中结点的大小，当l1的结点值小于l2的结点时，我们就需要将l2合并到l1上，把l2的结点一个一个拼到l1上，知道l2为为空时，循环就可以结束了。这个过程是重复的，所以我们这里可以使用递归操作，反之，当l2的结点小于l1时，就把l1拼接到l2上


```Python
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        """
        倒置链表
        :param pHead:
        :return:
        """
        # 判断当前节点是否为空或者下一个节点为空
        if not pHead or not pHead.next:
            return pHead
        # 初始化未节点为空
        last = None
        # 循环迭代头节点
        while pHead:
            # 创建一个中间节点接受头节点的下一个节点
            tmp = pHead.next
            # 将尾节点赋值给尾节点
            pHead.next = last
            # 将头节点赋值给尾节点
            last = pHead
            # 将中间节点赋值给头节点
            pHead = tmp
        return last
```

## 二叉树的镜像

### 题目描述

操作给定的二叉树，将其变换为源二叉树的镜像。

二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

### 分析

一般看到树的题都是使用递归处理最简单明了，转变为镜像数，我们很容易想到去交换树的左右子树，然后递归左子树和右子树即可

```Python
class Solution:
    def Mirror(self, root):
        """
        返回镜像树的根节点
        :param root:
        :return:
        """
        # 如果跟节点为空
        if not root:
            return None
        # 交换左子树和右子树
        root.left, root.right = root.right, root.left
        # 递归左右子树
        self.Mirror(root.left)
        self.Mirror(root.right)
```

## 顺时针打印矩阵

### 题目描述

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

### 分析

找出边界条件，将矩阵分为四个方向，注意每个方向上的结束条件


```Python
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > 2 * start and cols > 2 * start:
            endx = rows - 1 - start
            endy = cols - 1 - start
            for i in range(start, endy + 1):
                result.append(matrix[start][i])
            if start < endx:
                for i in range(start + 1, endx + 1):
                    result.append(matrix[i][endy])
            if start < endx and start < endy:
                for i in range(endy - 1, start - 1, -1):
                    result.append(matrix[endx][i])
            if start < endx - 1 and start < endy:
                for i in range(endx - 1, start, -1):
                    result.append(matrix[i][start])
            start += 1
        return result
```

## 包含min函数的栈

### 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

### 分析

得到最小元素的关键就是怎么去保存这个最小元素，这里在push的时候将插入的值作为键，当前最小值作为值作为一个元素插入栈。就可以得到每个元素插入的时候最小值是什么

(当然也可以使用单独的字段保存最小值)

```Python
class Solution:

    def __init__(self):
        self.stack = []

    def push(self, node):
        """
        推入元素
        使当前元素的值作为键，当前最小值作为值
        :param node:
        :return:
        """
        curMin = self.min()
        if curMin is None or node < curMin:
            curMin = node
        self.stack.append((node, curMin))

    def pop(self):
        self.stack.pop()

    def top(self):
        """
        弹出顶部元素的值
        :return:
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][0]

    def min(self):
        """
        得到最小栈中最小的元素
        :return:
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][1]
```

>注：
>- 上述测试在**Python3.5**中成功
>- 上述文字皆为个人看法，如有错误或建议请及时联系我


