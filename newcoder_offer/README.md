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


>注：
>- 上述测试在**Python3.5**中成功
>- 上述文字皆为个人看法，如有错误或建议请及时联系我


