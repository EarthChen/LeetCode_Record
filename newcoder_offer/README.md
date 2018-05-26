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

## 重建二叉树

### 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


### 分析
在前序遍历中找到跟节点，根据中序遍历中的跟节点的左右找到左右子树的元素，进行递归即可

```Python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        """
        根据前序和中序遍历重建二叉树
        :param pre:
        :param tin:
        :return:
        """
        if not pre and not tin:
            return None
        # 根据前序遍历获取到根节点
        root = TreeNode(pre[0])
        # 根据中序遍历得到根节点的索引
        i = tin.index(pre[0])
        # 　递归得到左子树（前序遍历的第１位到根节点索引＋１位，中序遍历的第０位到根节点的索引位）
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        # 　递归得到左子树（前序遍历的第根节点＋１位到最后一位，中序遍历的第根节点＋１到最后一位）
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root
```

## 用两个栈实现队列

### 题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

### 分析
在入队的时候均使用栈1存储，出队的时候先判断栈2是否为空，如果为空，将栈1的元素依次弹出到栈2，然后弹出栈2的元素

```Python
class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        # 直接向栈1压入元素
        self.stack1.append(node)

    def pop(self):
        # return xx
        # 如果栈2位空的情况
        if not self.stack2:
            # 迭代栈1，将栈1的元素弹出并压入栈2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            # 此时弹出栈2的元素
            return self.stack2.pop()
        # 如果栈1不为空，说明已经将元素压入栈2，直接弹出即可
        return self.stack2.pop()
```

## 旋转数组的最小数字

### 题目描述 

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

### 分析
使用py的内建函数直接求得最小值

```Python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        旋转数组的最小值
        :param rotateArray:
        :return:
        """
        if not rotateArray:
            return 0
        return min(rotateArray)
```

## 栈的压入、弹出序列

### 题目描述 

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

### 分析

使用一个辅助栈来存储，遍历入栈顺序依次添加到辅助栈，判断栈的长度且栈顶是都等于弹出序列

```Python
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False
        # 创建一个辅助栈
        stack = []
        for i in pushV:
            # 将遍历入栈顺序，添加到辅助栈中
            stack.append(i)
            # 如果栈不为空，且栈顶元素等于弹出序列
            while len(stack) and stack[-1] == popV[0]:
                # 出栈
                stack.pop()
                popV.pop(0)
        # 如果辅助栈为空
        if len(stack):
            return False
        return True
```

## 从上往下打印二叉树

### 题目描述 
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

### 分析
使用队列去存储中间值,使用while循环去遍历即可

```Python
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        result = []
        # 如果根节点为空
        if not root:
            return result
        # 将根节点放入列表中
        q = [root]
        # 当ｑ列表不为空
        while len(q):
            # 　将ｑ列表的第一个元素赋值给新节点
            node = q.pop(0)
            # 将节点的值添加到结果列表中
            result.append(node.val)
            # 如果节点有左子树
            if node.left:
                # 将节点的左子树放入ｑ列表
                q.append(node.left)
            if node.right:
                # 将节点的右子树放入ｑ列表
                q.append(node.right)
        return result
```

## 二叉搜索树的后序遍历序列

### 题目描述 

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

### 分析
根据后序遍历的特点，我们可以知道数组中的最后宇哥元素时根节点，有了根节点，我们可以找到列表中最后一个小于根节点的值的元素。遍历这个元素到数组的最后一个元素之间的元素(元素为根节点的右子树)，右子树的所有元素应该大于根节点，如果有小于根节点的元素，返回false，接下来递归数组中的左右元素

```Python
class Solution:
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        # 数组的最后元素是该树的根节点
        root = sequence[-1]
        left = 0
        # 找到最后一个小于根节点的元素
        while sequence[left] < root:
            left += 1
        # 遍历最后一个小于根节点的元素到根节点之前
        for i in range(left, length - 1):
            # 判断是否大于根节点(右子树元素)
            if sequence[i] < root:
                return False
        # 递归左右子树
        return self.VerifySquenceOfBST(sequence[:left]) \
               or self.VerifySquenceOfBST(sequence[left:length - 1])
```

## 二叉树中和为某一值的路径

### 题目描述

输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


### 分析
首先对特殊边界条件进行判断，然后分别递归左右子树，向下递归时需要使用目标值减去根节点的值，最后将左右子树的递归结果拼接为一个列表进行遍历，使用一个新列表去接受根节点加上遍历的元素值


```Python
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 如果是个空树
        if not root:
            return []
        # 如果根节点不为空，并且根节点的值等于指定值而且左右子树均为空
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        # 递归左子树
        left = self.FindPath(root.left, expectNumber - root.val)
        # 递归右子树
        right = self.FindPath(root.right, expectNumber - root.val)
        # 遍历拼接左右子树的结果
        for i in left + right:
            # 将根节点的值+i添加到res数组上
            res.append([root.val] + i)
        return res
```

## 复杂链表的复制

### 题目描述

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）



### 分析

这里给出的解法的核心就是使用两个字典保存随机节点和新老节点的对应，在需要构建的节点直接取出赋值


```Python
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        head = pHead
        p_head = None
        new_head = None

        # 保存随机节点和新老节点的字典
        random_dic = {}
        old_new_dic = {}

        # 当头节点不为空时
        while head:
            # 根据旧链表构造一个新节点
            node = RandomListNode(head.label)
            # 将头节点的随机指向的节点赋值给新节点的头节点
            node.random = head.random
            # 将节点对象的内存地址和头节点的id保存到字典中
            old_new_dic[id(head)] = id(node)
            # 将随机节点的对象地址和对象节点保存在随机字典中
            random_dic[id(node)] = node
            # 将头节点的下一个元素赋值给头节点
            head = head.next

            # 如果新头节点存在
            if new_head:
                # 将构造的新节点赋值给头节点的下一个节点
                new_head.next = node
                # 将新头节点的下一个节点赋值给头节点
                new_head = new_head.next
            else:
                # 头新节点不存在时，直接将构造的新节点赋值给头节点
                new_head = node
                # 将新构造的节点赋值给节点
                p_head = node
        new_head = p_head
        # 如果新头节点存在
        while new_head:
            # 并且头节点的随机指针不为空
            if new_head.random is not None:
                # 从随机字典中取出随机节点赋值给头节点的随机指针
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            # 将头节点的下一个节点赋值给头结点
            new_head = new_head.next
        # 返回头节点
        return p_head
```

## 二叉搜索树与双向链表

### 题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

### 分析
首先我们需要知道二叉搜索树的特点，也就是左小右大，我们需要递归处理左右子树，交换左右子树中的子节点使其成为链表，根节点在最中间

```Python
class Solution:
    def Convert(self, pRootOfTree):
        # 处理根节点为空
        if not pRootOfTree:
            return pRootOfTree
        # 只有根节点的情况
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while (left.right):
                left = left.right
            # 　交换节点的值
            pRootOfTree.left, left.right = left, pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while (right.left):
                right = right.left
            # 　交换节点的值
            pRootOfTree.right, right.left = right, pRootOfTree

        # 当左子树存在时
        while (pRootOfTree.left):
            # 左子树赋值给自己
            pRootOfTree = pRootOfTree.left
        # 返回链表的头节点
        return pRootOfTree
```


## 字符串的排列

### 题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。。

>输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

### 分析
使用标准库中的方法即可，重排序之后进行去重排序

```Python
import itertools


class Solution:
    def Permutation(self, ss):
        # 如果ss为空
        if not ss:
            return []
        # 使用标准库中的permutations进行全排序，使用map函数聚合
        # 使用set去重
        # 转为list并排序
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))
```

## 数组中出现次数超过一半的数字

### 题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0

### 分析

求数组长度的一半，然后遍历数组中每个元素的，判断是否大于数组长度的一半


```Python
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
```

## 最小的K个数

### 题目描述

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

### 分析
首先判断边界条件，k是否大于数组长度，简单处理可以对列表进行排序并取出前k个


```Python
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        return sorted(tinput)[:k]
```

## 整数中1出现的次数（从1到n整数中1出现的次

### 题目描述

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。

### 分析
设定整数点（如1、10、100等等）作为位置点i（对应n的各位、十位、百位等等），分别对每个数位上有多少包含1的点进行分析
 根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
 当i表示百位，且百位对应的数>=2,如n=31456,i=100，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31），每一次都包含100个连续的点，即共有(a%10+1)*100个点的百位为1
当i表示百位，且百位对应的数为1，如n=31156,i=100，则a=311,b=56，此时百位对应的就是1，则共有a%10(最高两位0-30)次是包含100个连续点，当最高两位为31（即a=311），本次只对应局部点00~56，共b+1次，所有点加起来共有（a%10*100）+(b+1)，这些点百位对应为1
  当i表示百位，且百位对应的数为0,如n=31056,i=100，则a=310,b=56，此时百位为1的次数有a/10=31（最高两位0~30）
综合以上三种情况，当百位对应0或>=2时，有(a+8)/10次包含所有100个点，还有当百位为1(a%10==1)，需要增加局部点b+1
之所以补8，是因为当百位为0，则a/10==(a+8)/10，当百位>=2，补8会产生进位位，效果等同于(a/10+1)


```Python
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        i = 1
        while i <= n:
            a = n / i
            b = n % i
            count += (a + 8) / 10 * i + (a % 10 == 1) * (b + 1)
            i *= 10
        return count
```



## 把数组排成最小的数

### 题目描述

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

### 分析

使用标准库的全排列方法将列表中的元素进行全排序，然后去重排序取第0个元素即可

```Python
import itertools

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = map(str, numbers)
        # 全排列去重转列表排序取最小值
        res = sorted(list(set(map(''.join, itertools.permutations(numbers)))))
        return res[0]
```


## 丑数

### 题目描述

把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数

### 分析

既然知道第一个丑数为1，并且丑数的因子只包含2 3 5，我们可以分别乘以2 3 5，来求出其中的最小值，放入丑数列表，最后取出最后一个即可

```Python
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
```


## 第一个只出现一次的字符

### 题目描述

在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

### 分析

当s为空时候，直接返回-1，当不为空的时候，遍历字符串，当从双向查找的索引值都相等，即找到所求

```Python
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == '':
            return -1
        for i in range(len(s)):
            # 当从前往后查找和从后向前查找时返回值相等时，即只出现了一次
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1
```


## 两个链表的第一个公共结点

### 题目描述

输入两个链表，找出它们的第一个公共结点。

### 分析

使用列表存储其中一个链表，遍历第二个链表判断是否在列表中

```Python
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        list1 = []
        node1 = pHead1
        node2 = pHead2
        # 使用一个列表存储第一个链表的所有节点
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        # 循环遍历第二个链表判断是否存在列表中
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next
```

## 数字在排序数组中出现的次数

### 题目描述

统计一个数字在排序数组中出现的次数。

### 分析

由于是排序的，所以可以想到二分查找，当然利用一些标准库函数也可以，但是不符合题意了


```Python
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
```


## 二叉树的深度

### 题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

### 分析

求深度，递归判断左右子树的深度，最后加上根节点即可


```Python
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
```


## 平衡二叉树

### 题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

### 分析

根据平衡二叉树的特点求解即可


```Python
class Solution:
    def IsBalanced_Solution(self, pRoot):
        """
        判断一个树是否为平衡二叉树
        当check函数的发挥值不等于-1时返回true，等于-1是返回false
        :param pRoot: TreeNode
        :return: bool
        """
        return self.check(pRoot) != -1

    def check(self, root):
        """
        检查结点
        :param root: TreeNode
        :return: int
        """
        # 结点为空时
        if root is None:
            return 0
        # 递归得出左子树的返回值
        left = self.check(root.left)
        # 递归得出右子树的返回值
        right = self.check(root.right)
        # 如果左子树不为平衡树或者右子树不为平衡二叉树，
        # 左右子树相减的值大于1(-1-(-1))左右子树不为平衡树的情况
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        # left right分别等于0或1的情况
        return 1 + max(left, right)
```


## 数组中只出现一次的数字

### 题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

### 分析

使用一个列表来保存元素，因为每个元素最多出现两次，当出现第二次的时候，删除该元素，最后列表中只会留下只出现一次的元素


```Python
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        """
        遍历数组，如果已存在的结果列表中就移除，不存在则添加
        :param array:
        :return:
        """
        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp
```


## 和为S的连续正数序列

### 题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

### 分析

这里给出的解法是最笨的方法，时间复杂度会比较高，也就是依次从0开始相加，直到等于所求的和。还可以根据序列的特点去求解，比如等差数列求和，，，可以相对降低时间复杂度


```Python
class Solution:
    def FindContinuousSequence(self, tsum):
        # 当要求的和的值小于3，不存在这样的序列
        if tsum < 3:
            return []
        s = []
        # 遍历从1到所求和之前的值
        for i in range(1, tsum):
            t = 0
            j = i
            # 从0开始依次相加，直到不小于和
            while t < tsum:
                t = t + j
                j = j + 1
            # 判断是否等于和
            if t == tsum:
                s.append(range(i, j))
        return s
```


## 和为S的两个数字

### 题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

### 分析

使用字典存储乘积和两个数的元组，由于递增排序，所以在字典中出现同样乘积的只保留第一组键值对。当结果字典不为空的时候，将字典进行排序取出第一组键值对的值


```Python
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
```


## 左旋转字符串

### 题目描述

汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

### 分析

左旋转，斟酌题意可以知道当n大于字符串长度或者小于0，字符串都是没有变化的，直接返回0即可。否则，将前n字符串拼接到后n位字符串后面即可


```Python
class Solution:
    def LeftRotateString(self, s, n):
        # 当n大于字符串长度或者小于0的时候，等于没有变
        if n >= len(s) or n <= 0:
            return s
        # 将字符串的前n位拼接到字符串的最后即可
        return s[n:] + s[:n]
```


## 翻转单词顺序列

### 题目描述

牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

### 分析

翻转单词，首先我们需要对字符串进行空格切分，然后将其逆序，再按空格拼接为字符串

```Python
class Solution:
    def ReverseSentence(self, s):
        # 使用空格进行字符串切割转换为列表
        l = s.split(' ')
        # 使用空格将字符串倒序拼成一个新的字符串
        return ' '.join(l[::-1])
```

## 求1+2+3+...+n

### 题目描述

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

### 分析

使用递归解决

```Python
class Solution:
    def Sum_Solution(self, n):
        if n == 1:
            return 1
        return n + self.Sum_Solution(n - 1)
```

## 不用加减乘除做加法

### 题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

### 分析

这里使用内置函数sum

（可以使用位运算，但是Python这里涉及到负数不知道怎么就报错了，就不展示代码了）

```Python
class Solution:
    def Add(self, num1, num2):
        return sum([num1, num2])
```

## 把字符串转换成整数

### 题目描述

将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

### 分析

首先判断边界条件，最后使用ord()将字符转为数字，计算。

(看答案有人使用int()函数直接解决，但个人觉得不怎么符合题意)

```Python
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        number = 0
        start = 0
        flage = 1
        if s[0] == '+':
            start = 1
        elif s[0] == '-':
            flage = -1
            start = 1
        # 遍历字符串
        for i in range(start, len(s)):
            # 如果不在0到9
            if s[i] < '0' or s[i] > '9':
                return 0
            else:
                # 转换为数字
                number = number * 10 + flage * (ord(s[i]) - ord('0'))
        return number
```

## 数组中重复的数字

### 题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2

### 分析

首先判断边界条件，遍历数组时，使用一个列表去保存遍历过的值，判断当前遍历的元素是否存在列表中，如果存在，将当前值保存，并返回true，窦泽将当前值保存在列表中

```Python
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # 边界条件
        if numbers is None or numbers == []:
            return False
        # 使用一个列表接收遍历过的值
        s = []
        for i in numbers:
            # 存在
            if i in s:
                duplication[0] = i
                return True
            s.append(i)
        return False
```

## 构建乘积数组

### 题目描述

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

### 分析

首先初始化b，然后遍历ab，判断当前遍历的索引是否相等，不相等时，将B[i]*A[i]赋值给B[i]

```Python
class Solution:
    def multiply(self, A):
        # 将b列表元素都初始化为1
        B = [1] * len(A)
        # 遍历a
        for i in range(len(A)):
            # 遍历b
            for j in range(len(B)):
                # 如果i不等于j
                if i != j:
                    B[i] *= A[j]
        return B
```


## 正则表达式匹配

### 题目描述

请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

### 分析

首先也是判断边界条件，当模式或者字符串为空的情况。

然后依次判断每个字符，判断模式串第二个字符是否为*,然后只需判断第一个模式串是否为.或者与字符相等，当满足条件时，递归判断从第二个开始的字符串。

如果模式串第二个字符串不为*时，则递归判断第三个开始的字符串

同时还需要判断只匹配一个字符的情况

```Python
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:  # 若均为空，返回true
            return True
        if len(s) > 0 and len(pattern) == 0:  # 若模式串为空，而字符串不为空，返回False
            return False
        if len(pattern) > 1 and pattern[1] == '*':  # 若模式串的第二个字符为*
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):  # 若s不为0，且第一个字符匹配
                return self.match(s[1:], pattern) or self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:])
            # 有三种情况：**表示模式串的第一个字符个数为2即重复了；*表示模式串的第一个字符个数为0；*表示模式串的第一个字符个数为1
            else:  # s的长度为0时，看模式串后面是否还有未匹配的项
                return self.match(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):  # 只匹配一个字符的情况
            return self.match(s[1:], pattern[1:])  # 继续匹配该字符之后的字符串
```


## 表示数值的字符串

### 题目描述

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

### 分析

使用float函数转为数字，当转换失败抛出异常时，返回false

或者使用正则表达式去判断

```Python
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            a = float(s)
            return True
        except:
            return False
```


## 字符流中第一个不重复的字符

### 题目描述

请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。

### 分析

使用字符串和一个字典去保存字符出现的次数(字符为键，次数为值)遍历字符串，判断字典中是否含有键为字符的元素，如果有，值为1时，返回即可。否则返回‘#’

```Python
class Solution:
    # 返回对应char
    def __init__(self):
        """
        使用一个字符串和一个字典保存字符串出现的次数
        """
        self.s = ''
        self.dict1 = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            # 如果键值对的值为1(出现的次数为1)
            if self.dict1[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # 每次将字符串加上新字符
        self.s = self.s + char
        # 判断当前字符是否是字典中的键
        if char in self.dict1:
            # 将对应的键值+1
            self.dict1[char] = self.dict1[char] + 1
        else:
            # 不存在即直接赋值为1
            self.dict1[char] = 1
```


## 链表中环的入口结点

### 题目描述

一个链表中包含环，请找出该链表的环的入口结点。

### 分析

使用一个列表保存遍历过的节点，遍历单链表判断是否在列表中。

```Python
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        if not pHead or not pHead.next:
            return None
        node = pHead
        while node:
            if node in tempList:
                return node
            else:
                tempList.append(node)
            node = node.next
```


## 删除链表中重复的结点

### 题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

### 分析

首先判断边界条件，当满足条件时，判断下当前节点的下一个节点是否等于当前节点，不等于的话递归继续得到下一个节点，当等于时，循环直到等于空或者不等于当前节点值，使当前节点的下一个节点指向不等于当前节点的节点。重复判断下一个节点是否等于当前节点

```Python
class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        # 如果下一个节点不等于当前节点
        if head1.val != pHead.val:
            # 递归得到下一个节点
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            # 如果下一个节点等于当前节点并且下一个节点不为空
            while pHead.val == head1.val and head1.next is not None:
                # 使下一个节点为下下个节点
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead
```


## 二叉树的下一个结点

### 题目描述

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

### 分析

分析中序遍历的特点，判断当前是否有左右子树，当有右子树时，则找出右子树的最左节点。当没右子树，则找第一个当前节点是父节点左孩子的节点

```Python
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return pNode
        # 如果有右子树，则找右子树的最左节点
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        # 没右子树，则找第一个当前节点是父节点左孩子的节点
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        # 退到了根节点仍没找到，则返回null
        return None
```


## 对称的二叉树

### 题目描述

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

### 分析

创建一个新方法，传入两颗数，分别判断头节点和左右子树的边界条件，然后递归判断当前左子树和右子树是否为对称的

```Python
class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymBT(pRoot, pRoot)

    def isSymBT(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.isSymBT(tree1.left, tree2.right) and self.isSymBT(tree1.right, tree2.left)

```


## 按之字形顺序打印二叉树

### 题目描述

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

### 分析

分别使用列表来保存遍历过的节点，下一层节点，结果。并且在设置一个标识符来判断当前应该是从左到右遍历还是从右向左遍历。

```Python
class Solution:
    def Print(self, pRoot):
        root = pRoot
        if not root:
            return []
        level = [root]
        # 使用一个列表保存结果
        result = []
        # 使用一个标识符标识左右遍历顺序
        left_to_right = False
        while level:
            # 保存当前节点值的列表
            cur_values = []
            # 保存下一层节点列表
            next_level = []
            # 　遍历层级节点
            for i in level:
                # 将当前遍历的节点值保存在当前节点值列表中
                cur_values.append(i.val)
                # 判断当前节点是否有左右子树，依次添加到下一层节点列表
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            # 　判断当前从左到右遍历还是从右到左遍历
            if left_to_right:
                cur_values.reverse()
            # 将遍历过节点值放入总结果列表中
            if cur_values:
                result.append(cur_values)
            # 将下一层节点付给当前层
            level = next_level
            # 将标识符倒置
            left_to_right = not left_to_right
        return result
```


## 把二叉树打印成多行

### 题目描述

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

### 分析

和上一题一样的思路，但是比之前少了一个顺序标识符，只需要从左到右遍历即可

```Python
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        root = pRoot
        level = [root]
        while level:
            cur_value = []
            next_level = []
            for i in level:
                cur_value.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if cur_value:
                result.append(cur_value)
            level = next_level
        return result
```

## 序列化二叉树

### 题目描述

请实现两个函数，分别用来序列化和反序列化二叉树

### 分析

序列化，就是将整个二叉树转换为字符串，这里将空节点转为‘＃’每个节点之间使用‘，’分割

反序列化，将序列化后的字符串创建一个二叉树

均使用递归解决，注意边界条件

```Python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = -1

    def Serialize(self, root):
        """
        对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
        不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替
        :param root:
        :return:
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        """
        对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树
        :param s:
        :return:
        """
        self.flag += 1

        l = s.split(',')
        if self.flag >= len(s):
            return None

        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
```


## 二叉搜索树的第k个结点

### 题目描述

给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

### 分析

首先根据二叉搜索树的特点得到整个节点的有序列表，然后在节点中取出相应节点即可

```Python
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k == 0:
            return None
        n = self.isorder(pRoot)
        if len(n) < k:
            return None
        else:
            # 返回第ｋ个节点
            return n[k - 1]

    def isorder(self, pRoot):
        re = []
        if not pRoot:
            return None
        if pRoot.left:
            # 如果左子树存在，递归得到所有子节点放入列表中
            re.extend(self.isorder(pRoot.left))
        # 将根节点放入列表中
        re.append(pRoot)
        if pRoot.right:
            # 如果右子树存在，递归得到所有子节点放入列表中
            re.extend(self.isorder(pRoot.right))
        return re
```


## 数据流中的中位数

### 题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

### 分析

在插入时，将其插入列表中并排序，然后根据奇数偶数求中位数

```Python
class Solution:
    x = []

    def Insert(self, num):
        # 将数字添加到列表中并排序
        self.x.append(num)
        self.x.sort()

    def GetMedian(self, x):
        # 得到长度
        n = len(self.x)
        # 判断奇数偶数
        if n % 2 == 1:
            return self.x[n // 2]
        else:
            return (self.x[n // 2 - 1] + self.x[n // 2]) / 2.0
```

## 滑动窗口的最大值

### 题目描述

给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

### 分析

首先判断边界条件，然后使用一个列表保存最大值，根据滑动的特点，每次将其向其向右移动，并求最大值，将其加入

```Python
class Solution:
    def maxInWindows(self, num, size):
        if size == 0 or size > len(num):
            return []
        max_num = []
        for i in range(len(num) - size + 1):
            max_num.append(max(num[i:i + size]))
        return max_num
```


## 连续子数组的最大和

### 题目描述

HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)

### 分析

本题由于有了负数的影响，在求序列之和时，会产生一些麻烦，最简单的思路，就是分别求出子序列的和并保存，最后得到最大的子序列之和，为了排除负数的影响，将值改为0即可。

```Python
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
```


##  数组中逆序对的数量

### 题目描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出
。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5
### 分析

先将原序列排序，然后从排完序的数组中取出最小的，它在原数组中的位置表示有多少比它大的数在它前面，每取出一个在原数组中删除该元素，保证后面取出的元素在原数组中是最小的，这样其位置才能表示有多少比它大的数在它前面，即逆序对数

```Python
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
```


##  扑克牌顺子

### 题目描述

LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。

### 分析

先统计王的数量，再把牌排序，如果后面一个数比前面一个数大于1以上，那么中间的差值就必须用王来补了。看王的数量够不够，如果够就返回true，否则返回false。


```Python
class Solution:
    def IsContinuous(self, numbers):
        # 如果列表为空
        if not numbers:
            return numbers
        # 将列表中大于0的元素生成新列表
        new_list = [i for i in numbers if i > 0]
        # 排序
        new_list.sort()
        # 如果新列表长度为1
        if len(new_list) == 1:
            return True
        n = 0
        # 遍历列表
        for j in range(len(new_list) - 1):
            # 如果后一个元素减去前一个元素大于0
            if (new_list[j + 1] - new_list[j]) > 0:
                # 将加入他们的差
                n += (new_list[j + 1] - new_list[j])
            else:
                return False
        if n <= 4:
            return True
        else:
            return False
```


## 孩子们的游戏(圆圈中最后剩下的数)

### 题目描述

每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

### 分析

将n个小朋友抽象成一个成环的列表，使用取模的方式求出当前m的索引值，然后弹出该索引上的元素，返回列表中的第一个元素。


```Python
class Solution:
    def LastRemaining_Solution(self, n, m):
        if not m or not n:
            return -1
        # 将n个小朋友索引转为列表
        res = range(n)
        i = 0
        # 当列表长度大于1
        while len(res) > 1:
            # 由于是环，可以用取模的方式得到m的索引
            i = (m + i - 1) % len(res)
            # 移除i位置的元素
            res.pop(i)
        # 返回第一个元素
        return res[0]
```


## 矩阵中的路径

### 题目描述

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

### 分析

 首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，在与第n个字符对应的格子的周围都没有找到第n+1个字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。当矩阵中坐标为（row,col）的格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)
以及(row+1,col)中去定位路径字符串中下一个字符如果4个相邻的格子都没有匹配字符串中下一个的字符，表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置


```Python
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的
        第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。
        除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
　　     由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，
        在与第n个字符对应的格子的周围都没有找到第n+1个字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。
　　     由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。
        当矩阵中坐标为（row,col）的格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)
        以及(row+1,col)中去定位路径字符串中下一个字符如果4个相邻的格子都没有匹配字符串中下一个的字符，
        表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。
　　     一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置
        :param matrix:
        :param rows:
        :param cols:
        :param path:
        :return:
        """
        # 遍历行列
        for i in range(rows):
            for j in range(cols):
                # 如果矩阵中的对应元素等于路径的第一个元素
                if matrix[i * cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True

    def find(self, matrix, rows, cols, path, i, j):
        """
        四个方向依次递归判断
        :param matrix:
        :param rows:
        :param cols:
        :param path:
        :param i:
        :param j:
        :return:
        """
        if not path:
            return True
        matrix[i * cols + j] = '0'
        if j + 1 < cols and matrix[i * cols + (j + 1)] == path[0]:
            return self.find(list(matrix), rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + (j - 1)] == path[0]:
            return self.find(list(matrix), rows, cols, path[1:], i, j - 1)
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find(list(matrix), rows, cols, path[1:], i + 1, j)
        if i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find(list(matrix), rows, cols, path[1:], i - 1, j)
        else:
            return False
```


# 机器人的运动范围

### 题目描述

地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

### 分析

将每次遍历过的格子使用字典记录下来，编写一个递归函数，递归判断当前遍历的格子向上下左右四个方向，在递归函数中还需判断各种边界条件


```Python
class Solution:
    def __init__(self):
        # 使用一个字典存储行列为键，值为1的键值对
        self.vis = {}

    def movingCount(self, threshold, rows, cols):
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        # 计算行坐标和列坐标的数位之和是否大于
        if row / 10 + row % 10 + col / 10 + col % 10 > threshold:
            return 0
        # 判断开始的行列是否大于总的行列
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        # 判断行列是否在字典中
        if (row, col) in self.vis:
            return 0
        # 将当前遍历的行列存入字典中
        self.vis[(row, col)] = 1
        # 将四个方向递归并且加上开始的第一个格子
        return 1 + self.moving(threshold, rows, cols, row - 1, col) \
               + self.moving(threshold, rows, cols, row + 1, col) \
               + self.moving(threshold, rows, cols, row, col - 1) \
               + self.moving(threshold, rows, cols, row, col + 1)
```


>注：
>- 上述测试在**Python3.5**中成功
>- 上述文字皆为个人看法，如有错误或建议请及时联系我


