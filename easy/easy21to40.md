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