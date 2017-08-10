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
class Solution:
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


## Merge Two Sorted Lists

题目:[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

>Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


题意分析:
将两个已排序的链表合并，并返回一个新的链表，新链表应该是由两个链表中的结点拼接起来的

###  思路分析
想要拼接链表，首先需要知道这个结点是什么样的结构，很容易想到，python中的单链表的结点应该如下所示:
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
当然题中也给出了这个结构。有了这个结构，就能知道我们需要得到结点的值才能进行比较。

又由于题目要求我们使用其中的一个结点将两个链表拼接起来，换句话说，就是将一个链表合并到另一个链表上，所以并不能创建一个新链表去进行操作。

当其中某一个链表为空时，只需要返回另一个链表即可，这种情况需要单独讨论

当两个链表均不为空时，我们需要去比较结点两个链表中结点的大小，当l1的结点值小于l2的结点时，我们就需要将l2合并到l1上，把l2的结点一个一个拼到l1上，知道l2为为空时，循环就可以结束了。这个过程是重复的，所以我们这里可以使用递归操作，反之，当l2的结点小于l1时，就把l1拼接到l2上

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        # 如果l1或l2有一个为空，则返回另一个
        if not l1 or not l2:
            return l1 or l2
        # 比较l1和l2的值的大小
        if l1.val < l2.val:
            # 将l2递归到l1上
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            # 将l1递归到l2上
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
```
用了递归的方式，减少了我们需要处理的循环等等

## Remove Duplicates from Sorted Array

题目:[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

>Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

>Do not allocate extra space for another array, you must do this in place with constant memory.

例子:
>Given input array nums = [1,1,2]
>Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length

题意分析:
去除有序数组中的重复元素，并返回去重之后的数组的长度

###  思路分析
由于我使用的是python，我首先想到的是用set集合去重，然后用len计算长度，立马兴奋的写下一行代码
```python
len(set(nums))
```
然而在这里会报错，所以只能考虑其他的办法。

还很容易想到的是用一个列表，字典之类的将我们遍历过的元素存起来，然后在用之后的元素与之比较，查看是否存在，存在就忽略，最后计算字典或者列表中元素的数量就能得到我们所需要的长度，但是同样与题目要求不符，题目要求不能使用分配额外的空间去解决。所以还得想别的办法

首先，数组或列表为空时，返回0，这个需要单独讨论，遍历这个列表是必须的。

我们可以假设新列表的长度为0，然后我们就能同时得到列表中第一个元素的值，在循环中我们可以用下一个与之比较，如果不一样，就将假设的新列表的长度+1，同时，由于有元素不一样，我们需要将新元素赋给之前相同的元素，也就是索引为新列表长度的元素，由于是排序的列表，我们不用担心，在未遍历的元素中还有之前已经遍历过的相同的元素。就这样从第二个开始遍历到最后一个，就能得到新列表的长度，但是由于我们是新列表的长度初始设为0，遍历又是从1开始，所以这个列表的长度最终应该+1


所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def removeDuplicates(self, nums):
        '''
        :param nums: list[int]
        :return:int
        '''
        # 如果数组为空，则返回0
        if not nums:
            return 0
        new_length = 0
        length = len(nums)
        # 从1到n-1开始循环遍历
        for i in range(1, length):
            # 如果i不等于nums[now_length](其实是i-1)
            if nums[i] != nums[new_length]:
                new_length += 1
                nums[new_length] = nums[i]
        return new_length + 1
```
这样我们就可以不用额外的空间，并且时间复杂度只有O(N-1)

## Remove Element

题目:[Remove Element](https://leetcode.com/problems/remove-element/description/)

>Given an array and a value, remove all instances of that value in place and return the new length.
>Do not allocate extra space for another array, you must do this in place with constant memory.
>The order of elements can be changed. It doesn't matter what you leave beyond the new length.

例子:
>Given input array nums = [3,2,2,3], val = 3
>Your function should return length = 2, with the first two elements of nums being 2

题意分析:
题意为给你一个数组，再给你一个值，删除所有和这个值相等的元素，返回新列表的长度，要求不能在使用额外的数组，只能操作这一个数组。

###  思路分析
本来我想的很简单，既然只是要返回长度，那我也可以不删除，只计算长度啊，抱着侥幸的心里尝试了最简单的办法，声明一个长度的变量，并设置初始值为0，循环遍历数组中所有元素，如果元素不与目标值相等就+1。提交之后发现并不能通过，那就是说，我们在返回长度的同时，也需要把元数组进行删除。

既然要删除元素，我想到了之前做过的[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)这一题，只不过这题要求是去除重复元素，同样都是去除元素，思想也有些类似，这题可以想象成已经给你了一个重复元素，我们我们可以套用之前的解法，做一点变化即可。

同样声明一个长度为0，因为是删除指定元素，所以数组为空的时候也不用担心，那就返回0嘛，所以这次也不需要对0进行单独讨论了，同样我们需要对数组进行循环遍历，如果该下标元素不等于目标值的话，我们就把该下标元素赋值给声明的长度作为下标的元素，然后将长度+1，这样我们就可以完成操作了。在程序最后返回长度即可。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def removeElement(self, nums, val):
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length, nums
```
这样我们就可以不用额外的空间，时间复杂度为O(N)


## Maximum Subarray

题目:[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

>Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

例子:
```text
given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6
```

题意分析:
求出一个整形列表中几个连续元素的和

###  思路分析
想要得到和，首先我们肯定要求和，想知道若干个元素的和，还得求出最大的和，意味着我们肯定要循环。

方法一:
很容易想到我们可以先先计算一个元素的和，然后循环得到这个元素与后续所有元素的和，并求出其中的最大值，这很简单，只需要当和大于假定的最大值时，更新最大值即可。这就得到了以一个元素开始与后续子元素其中的最大值。

想要得到整个列表中哪几个连续元素的和最大，我们还需要对所有元素进行循环，也就是在内循环以某个元素开始的最大值，在外循环得到以所有元素的最大值。

因为方法一的进行了两次循环，时间复杂度较高，为此我们需要想办法进行一次循环就得到我们需要的值。

方法二：
要达到目的，循环肯定少不了，既然我们不需要得到是哪几个元素的和最大，我们也就没必要进行两此循环，来得到是从那个索引开始到那个索引结束。

首先，我们声明两个变量，一个为循环当前的最大值，一个为我们需要的最大值，初始都将他们赋为列表的第一个元素（需要对为列表单独讨论）。

我们不需要得到元素列表，所以直接迭代列表元素即可，计算当前元素与当前的最大值+当前元素的和，并将他们俩之间的最大值赋值给当前最大值。

然后再将当前最大值与需要的最大值进行比较，把其中的最大值赋值给需要的最大值。循环结束就能得到我们需要的。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def maxSubArray(self, nums):
        """
        计算列表中连续子数组的最大和
        :param nums: list[int]
        :return: int
        """
        start = 0
        stop = 0
        length = len(nums)
        if length == 1:
            return sum(nums)
        largest_sum = nums[0]
        for i in range(0, length):
            max_sum = nums[0]
            for j in range(i, length):
                ij_sum = sum(nums[i: j + 1])
                if ij_sum > max_sum:
                    stop = j
                    max_sum = ij_sum
            if max_sum > largest_sum:
                start = i
                largest_sum = max_sum
        return largest_sum
```
时间复杂度较高为O(N^2),但可以得到最大和的元素列表

#### 方法二
```python
class Solution:
    def maxSubArray(self, nums):
        """
        计算列表中连续子数组的最大和
        :param nums: list[int]
        :return: int
        """
        if not nums:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            # 计算当前的和与i相加之后的和比较的最大值
            cur_sum = max(i, cur_sum + i)
            # 计算当前和与最大和比较的最大值
            max_sum = max(max_sum, cur_sum)
        return max_sum
```
一次循环，时间复杂度为O(N)，不能轻易得到元素列表

## Count and Say

题目:[Count and Say](https://leetcode.com/problems/count-and-say/description/)

>The count-and-say sequence is the sequence of integers with the first five terms as following:
```text
1.     1
2.     11
3.     21
4.     1211
5.     111221
```
>1 is read off as "one 1" or 11.
>11 is read off as "two 1s" or 21.
>21 is read off as "one 2, then one 1" or 1211.
>Given an integer n, generate the nth term of the count-and-say sequence.

例子:
```text
Input: 1
Output: "1"

Input: 4
Output: "1211"
```

题意分析:
第n次结果是对n-1次结果的解释。例如第4次的结果为1211，参照第3次结果，可以解释为一个2，一个1，就形成了1211，一次类推

###  思路分析
在我们掌握了规律之后，我们发现下一次的结果总由上一次的结果所决定，很容易想到可以用递归处理，如果采用递归，当然我们也需要知道结束标志，不然就会一直死循环下去了，这里很明显，结束标志就是当n为1或者0时，分别返回1或者空。

当需要求第n次结果时，我们可以获取递归调用第n-1次的结果进行处理，对上一次计算结果进行处理，这里就是对上一次计算结果解释。

所以我们可以有以下解法
#### 方法一
```python
class Solution:
    def countAndSay(self, n):
        """

        :param n: int
        :return: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        # 得到上一次的结果
        n1_str = self.countAndSay(n - 1)
        # 末尾字符赋值为上一次结果的第一个字符
        last = n1_str[0]
        cnt = 1
        n_str = ''
        # 从索引1开始迭代
        for i in range(1, len(n1_str)):
            # 如果当前元素等于初始末尾字符(上一次结果的第一个字符)
            if n1_str[i] == last:
                cnt += 1
            else:
                n_str = n_str + str(cnt)
                n_str = n_str + last
                # 将数量重置为1
                cnt = 1
                last = n1_str[i]
        n_str = n_str + str(cnt)
        n_str = n_str + last
        return n_str
```
这样就用递归的方式很简单的得到了结果。

当然我们也可以用求下一次结果的方式，只需要执行n-1次即可。
