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

## Reverse Integer

题目:[Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)

>Reverse digits of an integer.

例子:
```text
Example1: x = 123, return 321
Example2: x = -123, return -321
```
>注:The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

题意分析:
题目很简单，将数字倒置而已，最后结果要求判断是否为32位有符号整数

###  思路分析
想要倒置，又由于是int类型，我们可以使用除10求余的方式，循环求余，在每一步求出的余数放到一个数组李存起来，最后在将数组拼起来成为一个int类型整数。

但是，以上方法想想就很复杂，操作起来也很麻烦，想到基本每种语言都带有字符串倒置的方法，我们可以先将数字转换为字符串，在调用内置方法倒置字符串。如果是传入的x是负数，在将其转为为负数即可

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def reverse(self, x):
        # 对x判断为正还是为负
        if x < 0:
            x = abs(x)
            # 先将数字转为字符串，再用反向切片操作(其他语言也都有字符串倒置函数)
            return self.isOverFlows(-int(str(x)[::-1]))
        else:
            return self.isOverFlows(int(str(x)[::-1]))

    # 判断x是否在32位有符号数
    def isOverFlows(self, x):
        if pow(-2, 31) < x < pow(2, 31):
            return x
        return 0
```
使用了内置的字符串高效反向切片方法，并且将判断结果是否是属于32位有符号数分离出一个方法，减少耦合


## Palindrome Number

题目:[Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

>Determine whether an integer is a palindrome. Do this without extra space.

题意分析:
判断一个整形是否是回文，不能使用额外空间

###  思路分析
判断回文，首先需要知道回文的定义，就是正向和反向都一样的数字，也就是说这个数字需要前后对称，所以我们只需要用每个下标和它对称的下标上的数进行比较是否相等，如果不相等就不是回文，如果每个下标和对称位都相等就是回文，简单点可以直接从0循环到n-1，此时时间复杂度是O(N)，但其实只需要循环到一半即可，因为如果超过一半就会重复了，没有任何意义。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def isPalindrome(self, x):
        # 将数字转换为字符串
        x = str(x)
        # 得到字符串的长度
        n = len(x)
        # 对字符串进行迭代
        for i in range(n):
            # 判断头和尾是否相等并且头要小于尾
            if x[i] != x[n - i - 1] and i < n - i - 1:
                return False
        return True
```
很明显，此方法时间复杂度是O(N/2)，算较好的方法


## Longest Common Prefix

题目:[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

>Write a function to find the longest common prefix string amongst an array of strings..

题意分析:
求出一个字符串数组中所有字符串的最长共同前缀，如
['aaa','ab']  ==> a
['aaa']  ==> aaa
[]==> ''

###  思路分析
题目想要我们求出字符串数组中，所有字符串之间的共同的最长前缀，
想要求出最长的，这个最长的前缀，范围肯定是0到所有字符串中最短的字符串长度，所以得到最短的字符串和它自身的长度是很关键的，如果没有最短长度，我们根本不会知道循环的次数，如果随意选择一个字符串进行循环，如果这个字符串较长，就会造成越界错误

所以我们首先需要得到最短字符串和它自身的长度，来确定外循环次数，内循环去循环遍历每个字符串。

要得到最长共同前缀，其实这个和在一个数组里求最大的数的思路一样，我们需要先设第一个值为最大值，后面值分别与设的最大值相比较，如果比假设的最大值还要大，就需要更新假设最大值。

这里也一样，我们首先假设最长共同前缀为最短字符串的前1个字符，在内循环中判断每个字符的前i+1个子字符串是否等于假设的最长共同前缀，如果不相同，我们还需要判断当前i+1是否等于1，如果等于，那就是第一个字符都不相同，那就需要返回空，如果都相同，需要判断当前最长共同前缀是否等于最短字符串，如果等于，说明最长共同子串等于最短字符串，否则需要更新最长共同前缀，将其赋值为前i+1+1位的子字符串。进入下一次外循环。

在外循环中更新了最长共同前缀之后，在进入内循环判断，如果前i+1位子串不等于最长共同前缀，那就得返回前i位子串，此时前为i为子串即为最长共同前缀。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def longestCommonPrefix(self, strs):
        # 判断字符串列表是否为空
        if not strs:
            return ''
        # 计算字符串列表中最短的字符串
        min_str = min(strs)
        # 计算最短字符串的长度
        min_length = len(min_str)
        # 初始令最长共同前缀字符串为最短字符串的第一个字符
        max_common_str = min_str[:1]
        for i in range(min_length):
            for str in strs:
                # 判断字符串列表中每个字符串的前i+1位是否与最长共同字符串相同
                # 不同则判断当前字符串是否为第1个，是则返回空，不是则返回前i位字符串
                if str[:i + 1] != max_common_str:
                    if i == 0:
                        return ''
                    return str[:i]
            # 当每个字符串前i+1位都与共同前缀字符相同时，判断字符串是否最短字符串相同
            # 相同则返回最长共同前缀字符
            if min_str == max_common_str:
                return max_common_str
            # 不相同则返回前i+1+1位字符串(使字符串向后移动一位)
            max_common_str = min_str[:i + 1 + 1]
        return max_common_str
```
此解法时间复杂度是O(N^2)，目前我想不到更好的解法。。但是leetcode能通过

## Valid Parentheses

题目:[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

>The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


题意分析:
判断一个只有字符'(', ')', '{', '}', '[' 和 ']'的字符串，并且每对括号都需要正确的关闭，也就是说括号需要成对出现

###  思路分析
判断成对出现的东西，我们很容易想到栈（先进后出）这种数据结构。

括号亦是如此，如果出现左括号，我们就将其入栈，当在出现了右括号，我们在将其出栈，如果最后的栈为空，即括号刚好是成对出现的。

但我们还需要判断三种括号之间的对应关系（即左小括号对应右小括号等），为了实现这种需求，在python里可以使用字典(java里可以使用map)存储对应关系。

循环字符串时，如果当前字符为左字符串，则向栈(列表/数组)尾部加上这个字符，如果不等于左括号，则判断此时栈是否为空或者当前的右括号字符在字典中所对应的左括号是否等于出栈的元素，如果不相等，则返回false

循环完毕还需要判断栈是否为空，如果为空，则返回true，反之，返回false

所以我们可以有以下解法
#### 方法一
```python
lass Solution:
    def isValid(self, s):
        '''
        :param s: str
        :return: bool
        '''
        left_char = '({['
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # 初始化一个空列表作为栈
        stack = []
        # 循环遍历字符串
        for i in s:
            # 如果字符是左括号就入栈
            if i in left_char:
                stack.append(i)
            else:
                # 如果也想加上对其他字符串匹配
                # if i in mp.keys():
                    # 栈为空或者传入的右括号不等于栈尾的左括号，即不符合条件
                if not stack or mp[i] != stack.pop():
                    return False
        # 判断栈是否为空，为空即成立
        if not stack:
            return True
        return False
```
用列表来替代模拟栈，时间复杂度为O(N)，顺利通过leetcode检测