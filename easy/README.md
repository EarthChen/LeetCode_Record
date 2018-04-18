# LeetCode_Record(easy 21-40)


## Binary Tree Level Order Traversal II
题目:[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)

>Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

例子:
```text
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

题意分析:
给定一个二叉树，返回自底向上遍历结点的值

###  思路分析
相等于特殊的按层遍历，在基本的按层遍历树可以选择用栈或者队列来保存每一层的结点。在这里我们选择使用栈。并且使用列表来模拟栈，在使用一个列表来保存需要返回的结果。

首先，初始化需要将根结点与level为0的元组存入列表中，循环这个栈，不为空的话，在栈的尾部弹出一个元素，第一次也就是弹出的根结点和level层数。

得到弹出的结点，判断其是否为空，如果不为空，判断此时结果列表的长度，也就是已经遍历过的层数，

如果小于当前层数+1，也就是在结果列表的第一个位置插入一个列表。如果大于当前level+1，我们就可以在结果列表中放入合适的结点的值。然后只需要在栈中压入当前结点的左子树和当前层数level+1的元组，和右子树和当前层数level+1的元组。最后返回结果列表即可。

#### 方法一
 很容易想到我们可以遍历两次数组，在内循环中判断两次循环中的数相加是否等于target
```python
class Solution:
    def levelOrderBottom(self, root):
        """
        返回节点值的自底向上的顺序遍历。（从左到右，从叶到根逐级地）
        :param root: TreeNode
        :return: list[list[int]]
        """
        stack = [(root, 0)]
        res = []
        # 如果栈不为空
        while stack:
            # 将栈中最后一个元素弹出
            node, level = stack.pop()
            # 如果该结点存在
            if node:
                # 如果结果列表的长度小于层数+1
                if len(res) < level + 1:
                    res.insert(0, [])
                # 将当前结点的值添加在结果列表中
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res
```
使用队列的话，方式其实也是大同小异，这里就不在阐述。


## Convert Sorted Array to Binary Search Tree
题目:[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


题意分析:
给定一个数组，元素按升序排序，将其转换为高度平衡的BST。

###  思路分析
想要转换成平衡二叉树，首先我们需要知道什么叫做平衡二叉树，知道了bst是深才能开始思考与讨论。
>平衡二叉树（Self-balancing binary search tree）又被称为AVL树（有别于AVL算法），且具有以下性质：它是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树

平衡二叉树主要的特点就是“棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树”,知道了这个，题目又要求我们把一个已经排序的数组(列表)作为整个二叉树的值。

所以我们可以找出数组中的中值，把他作为根，把小于中值的作为左子树，大于中值的作为右子树，在利用递归的思想，从左子树中找到左子树的根，在右子树中找到右子树的根，就可以得到我们所需要的平衡二叉树。

所以我们可以有以下解法
#### 方法一
 很容易想到我们可以遍历两次数组，在内循环中判断两次循环中的数相加是否等于target
```python
class Solution:
    def sortedArrayToBST(self, num):
        """
        将已排序的数组转换为高度平衡二叉树
        :param num: list[int]
        :return: TreeNode
        """
        # 如果列表为空
        if not num:
            return None
        # 列表中间的值为列表长度整数2
        mid = len(num) // 2
        # 生成一个以中值为结点的值的作为根结点
        root = TreeNode(num[mid])
        # 递归求出
        # 左子树为小于中间值一部分
        root.left = self.sortedArrayToBST(num[:mid])
        # 右子树为大于中间值的一部分
        root.right = self.sortedArrayToBST(num[mid + 1:])
        return root
```


## Balanced Binary Tree
题目:[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

>Given a binary tree, determine if it is height-balanced.
>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


题意分析:
给定一个二叉树，判断其是否是平衡二叉树

###  思路分析
在上一题的分析中，我们已经知道了什么叫做平衡二叉树。题目给出的方法返回值的bool类型，不利于我们去循环递归的判断它。我们可以单独写一个check函数，其返回值是int类型。当函数返回-1时，该二叉树为非平衡二叉树，当函数返回值不为-1时，该二叉树为平衡二叉树。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def isBalanced(self, root):
        """
        判断一个树是否为平衡二叉树
        当check函数的发挥值不等于-1时返回true，等于-1是返回false
        :param root: TreeNode
        :return: bool
        """
        return self.check(root) != -1

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
        # 左右子树想减的值大于1(-1-(-1))左右子树不为平衡树的情况
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        # left right分别等于0或1的情况
        return 1 + max(left, right)
```


## Minimum Depth of Binary Tree
题目:[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

>Given a binary tree, find its minimum depth.
>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


题意分析:
求出二叉树的最小深度

###  思路分析
如果该树为空，需要单独讨论，返回深度为0.递归调用自己，传入根节点的左子树和右子树，如果其中有空节点，那么此时的left或者right就有值为0，既然求的是最小的深度，那么就可以返回该子树的深度。如果两个值均不为0了，那么就返回左子树和右子树深度的最小值，最后加上子树到根节点的1，即为最小深度。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def minDepth(self, root):
        # 如果是空树
        if not root:
            return 0
        # 递归求出子节点的深度
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 如果节点为空
        if left == 0 or right == 0:
            return left + right + 1
        # 不为空情况下计算左右子树的最小深度
        return min(left, right) + 1
```



## Path Sum
题目:[Path Sum](https://leetcode.com/problems/path-sum/description/)

>Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.


例子：
```text
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
```


题意分析:
题意还是很清楚的，给定一颗二叉树，在给定一个和，判断从根节点到叶子节点之间的路径和是否有等于给定的sum。

###  思路分析
对于空树，也就是只有根节点并且根节点为空，或者树中只有根节点，这两种情况都需要单独讨论。

对于空树，我们可以直接返回False不等于即可。

对于只有根节点的树，我们需要判断一下，该节点的值是否等于sum，等于就返回True

对特殊情况讨论完毕，我们就可以递归判断左子树和右子树的情况了，传入的sum需要用原来的sum-根节点的值。题目只要去判断是否有，所有我们用或去连接即可

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def hasPathSum(self, root, sum):
        """
        判断从根到叶子节点的值之和是否有等于sum的
        :param root: TreeNode
        :param sum: int
        :return: bool
        """
        # 如果是空树
        if not root:
            return False
        # 如果只有根节点，并且根节点的值等于sum
        if root.val == sum and not root.left and not root.right:
            return True
        # 递归判断对左右节点的情况，每次需要将sum减去节点的值
        return self.hasPathSum(root.left, sum - root.val) \
               or self.hasPathSum(root.right, sum - root.val)

```


## Pascal's Triangle
题目:[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)

>Given numRows, generate the first numRows of Pascal's triangle.


例子：
```text
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```


题意分析:
给定一个行数，生成一个帕斯卡三角形。

###  思路分析
如果不看例子，我们估计不知道什么叫帕斯卡三角形，题目也给出了我们一个例子。我们需要从每一行中找出规律，才能得到结果。

很容易可以看出，每一行第i位上的数字，等于上一行的i位数加上i+1上的数。

同时我们可以看到，每一行第一个数都是1

我们在求出每一行的列表之后，放入到保存所有行的列表中即可。

所以我们可以有以下解法
#### 方法一
```python
import copy


class Solution:
    def generate(self, numRows):
        # 最外侧的列表
        allrows = []
        # 每一行的列表
        row = []
        # 循环迭代每一行
        for i in range(numRows):
            # 像每行的第一个元素插入1
            row.insert(0, 1)
            # 对该行进行迭代(1开始因为已经插入了1，该行的长度-1因为保留了上一行的参数)
            for j in range(1, len(row) - 1):
                # 其中的参数等于索引为j和j+1位置的和
                row[j] = row[j] + row[j + 1]
            # 进行深拷贝，如果不进行深拷贝，Python会一直操作的是一个row最后只会append一个相同的row
            allrows.append(copy.deepcopy(row))
        return allrows
```
这段代码中涉及都了一个深拷贝的问题，因为我每一行的列表row，一直是一个，当每次循环操作的是同一个row，如果不使用深拷贝，最后append到列表中的都是最后一行的值，所以这里使用深拷贝，将每一行的值拷贝出来append到列表中。


## Pascal's Triangle II
题目:[Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)

>Given an index k, return the kth row of the Pascal's triangle.

例子：

```text
For example, given k = 3,
Return [1,3,3,1].
```



题意分析:
给定一个行数，生成帕斯卡三角形该行的数。

###  思路分析
这一题其实只是上一题的一部分，生成第n行的列表即可。

首先，每一行的第一个数都是1，我们就可以创建一个第一个元素为1的列表。然后就可以循环行数，这里可以使用列表推导式。

可以在该行的列表前面加上[0]，再在该行的列表后面加上[0]，然后使用zip()函数，将生成的两个新列表合并起来，用x和y分别取第一列的两个值，并求出x+y的和作为列表的第一个元素，将第二列也分别作为x和y进行同样的操作。最后得到的就是帕斯卡三角形该行的数。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def getRow(self, rowIndex):
        """
        计算帕斯卡三角形的制定行数的元素
        :param rowIndex: int
        :return: list
        """
        row = [1]
        for i in range(rowIndex):
            # 使用列表推导式迭代x+y的值
            # 其中x和y分别等于[0] + row和row + [0]的第一列和第二列
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
```


## Valid Palindrome
题目:[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

例子：
```text
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
```

>Note:
>- Have you consider that the string might be empty? This is a good question to ask during an interview.
>- For the purpose of this problem, we define empty string as valid palindrome.


题意分析:
判断一个字符串是否是回文，只考虑字母和数字，不考虑其他字符。

###  思路分析
又是一个求回文的题目，有点不同的就是，在字符串中添加了一些我们需要忽略的字符，最容易想到的方法就是将这些字符去掉，我们去判断新的字符串是否是回文，但是这样无疑增加了时间和空间复杂度。

为了解决那个问题，我们得在一次循环中解决，并且不能创建新的字符串，所以，我们只能忽略它。

我们可以先定义两个下标，一个表示表示开始下标，一个表示结束下标，因为求回文，只需要循环一半，并且开始下标小于结束下标，

因为我们不知道循环的次数，所以我们使用while循环，在这个循环内部我们需要找到符合属于字母和数字的字符最开始的下标是多少，如果第一个字符不属于字母或数字，那么将开始下标+1，依次类推，直到找到第一个属于字母或数字的字符下标，结束下标也一样，只不过当不符合要求时是将下标-1.

得到有效的开始下标和结束下标，我们就可以进行比较了，因为这里还忽略大小写，去比较两个字符是否相等就可以了，如果不相等，直接返回False

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def isPalindrome(self, s):
        """
        判断字符串是否是回文(只考虑字母和数字)
        :param s: str
        :return: bool
        """
        # 分别得到第一个和最后一个字符的索引
        i, r = 0, len(s) - 1
        # 判断回文只需要判断一半
        while i < r:
            # 当左边字符索引小鱼右边字符串并且
            # 左字符串属于字母和数字时
            while i < r and not s[i].isalnum():
                i += 1
            # 当左边字符索引小鱼右边字符串并且
            # 右字符串属于字母和数字时
            while i < r and not s[r].isalnum():
                r -= 1
            # 为了判断相等，均转换为小写去判断是否相等
            if s[i].lower() != s[r].lower():
                return False
            # 左字符向后移动一个
            i += 1
            # 右字符向前移动
            r -= 1
        return True
```



## Single Number
题目:[Single Number](https://leetcode.com/problems/single-number/description/)

>Given an array of integers, every element appears twice except for one. Find that single one.


>Note:
>- Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


题意分析:
给定一个列表，其中除了一个元素，其他元素都有两个，找出这个只有一个的元素(不使用额外的空间)

###  思路分析
想找出唯一的元素，最开始很容易想到的是循环每一个元素，然后判断该元素是否在剩下的列中中还存在，这种方式可以解决其他元素不只出现两次的情况，

但是这题比较特殊，除本身外，其他元素出现的次数是一致的，并且元素还都是int类型。所以就可以用一种比较投机取巧的办法。

我们可以先将该列表去重，这样所有元素就只出现了一次，然后我们将其求和并乘以2，这样我们就得到了两倍的和，然后我们在求一个元列表的和，这两者的差就是只出现了一次的元素


所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def singleNumber(self, nums):
        """
        找到数组只只出现了一次的元素(其他元素都出现了两次)
        :param nums: list[int]
        :return: int
        """
        # 使用set()去重把每个元素都得到一个
        # 求出所有单个元素的和,求出两倍的值
        # 再减去未去重时所有元素的和
        return 2 * sum(set(nums)) - sum(nums)
```


## Linked List Cycle
题目:[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

>Given a linked list, determine if it has a cycle in it.


>Note:
>- Can you solve it without using extra space?


题意分析:
判断单链表中是否有环。不使用额外空间

###  思路分析
判断列表是否有环，一个链表如果有环，那么至少是三个节点组成，第三个指向第一个。所以我们这里可以使用快慢指针的概念，慢指针一次移动一个节点，快指针一次移动两个节点，在快指针存在并且快指针的下一个节点不为空的时候循环，判断快指针的节点是否等于慢指针的节点。

当单链表为空，或者只有头节点时需要单独处理。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def hasCycle(self, head):
        """
        判断单链表中是否有环(不使用额外的空间)
        :param head: ListNode
        :return: bool
        """
        # 如果链表的头节点或者头节点的下一个节点为空
        if not head or not head.next:
            return False
        # 使用快慢指针
        # 慢指针一次向前移动一个节点
        slow = head
        # 快指针一次向前移动两个节点
        fast = head.next
        # 如果快指针存在并且快指针的下一个节点也存在
        while fast and fast.next:
            # 使慢指针向后移动一个节点
            slow = slow.next
            # 使快指针向后移动两个节点
            fast = fast.next.next
            # 如果快指针等于慢指针，即有环
            if slow == fast:
                return True
        return False
```


## Min Stack
题目:[Min Stack](https://leetcode.com/problems/min-stack/description/)

>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>- push(x) -- Push element x onto stack.
>- pop() -- Removes the element on top of the stack.
>- top() -- Get the top element.
>- getMin() -- Retrieve the minimum element in the stack.


例子:
```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```


题意分析:
设计一个栈，支持一些基本操作

###  思路分析
使用列表去模拟栈即可。

所以我们可以有以下解法
#### 方法一
```python
class MinStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        """
        向栈种推入一个元素
        :param x: int
        :return: void
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        """
        弹出一个元素
        :return: void
        """
        self.q.pop()

    def top(self):
        """
        得到栈顶元素
        :return: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self):
        """
        得到最小栈中最小的元素
        :return: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]
```