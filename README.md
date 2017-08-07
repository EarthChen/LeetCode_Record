# LeetCode_Record

## Two Sum
题目:[two sum](https://leetcode.com/problems/two-sum/description/)


>Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

例子:
```text
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

题意分析:
找出数组numbers中的两个数，它们的和为给定的一个数target，并返回这两个数的索引(不需要去重)

###  思路分析
题目要求说白了就是找出这个给的数组中有哪两个数相加等于目标结果
#### 方法一
 很容易想到我们可以遍历两次数组，在内循环中判断两次循环中的数相加是否等于target
```python
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)  # 计算输入的列表长度
        for i in range(length):
            for j in range(length):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
这是一种很简单很容易能想到的方法，但此方法的时间复杂度是O(N^2),在leetcode会超时，所以不行，想要通过，肯定要降低时间复杂度

为了降低时间复杂度，我们可以牺牲空间来换取时间，使用一次循环，将时间复杂度降为O(N)，所以我们可以有以下解法

#### 方法二
可以使用字段存储遍历过的num和它的下标放置一个字典中，在循环这个列表，用目标结果target减正在循环的这个数，并判断结果是否在字典中(即是否循已经遍历过)，如果结果存在如字典中，即找到相加等于结果的两个值，如果不存在，即把值和对应下标存入字典中
```python
class Solution:
    def twoSum(self, nums, target):
        arr = {}  # 使用字典存储遍历过的num和对应下标{num:index}
        length = len(nums)  # 计算输入的列表长度
        for i in range(length):
            if (target - nums[i]) in arr:
                # 如果target-当前num的差在arr中，则表示已经找到答案，返回结果即可
                return [arr[target - nums[i]], i]
            # 否则，将该num及其下标存入arr中
            arr[nums[i]] = i
```
此时就牺牲了一个字典的空间，来换取了O(N)的复杂度，在leetcode也能通过