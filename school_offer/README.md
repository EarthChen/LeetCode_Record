## 合唱团

### 题目描述

有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

### 输入描述

每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。

### 输出描述
输出一行表示最大的乘积

### 示例

1. 输入
3
7 4 7
2 50

2. 输出

49



### 分析

定义fm[k][i]表示当选中了k个学生，并且以第i个学生为结尾，所产生的最大乘积；fn[k][i]表示 当选中了k个学生，并且以第i个学生为结尾，所产生的最小乘积；那么fm[k+1][i+1]=max(fm[k][i]*stu[i+1],fn[k][i]*stu[i+1])，即当选中了k个学生后，再选择第i+1编号学生，所产生的最大乘积；然而，并不能保证上一次选择的就是第i个学生，所以要遍历子数组fm[k]，令j从i到1，并且j与i+1之间小于间隔D，遍历fm[k][j]，以及fn[k][j]；
同理fn[k+1][i+1]=min(fn[k][i]*stu[i+1],fm[k][i]*stu[i+1])。最后，遍历一遍fm[K][i]求得最大值（i从1～N）。

```Python
# 获取输入
n = int(input())
arr = map(int, input().split())
K, D = map(int, input().split())

# fm[k][i]表示当选中了k个学生，并且以第i个学生为结尾，所产生的最大乘积；
fm = [([0] * n) for i in range(K)]  # k*d

#  fn[k][i]表示 当选中了k个学生，并且以第i个学生为结尾，所产生的最小乘积；
fn = [([0] * n) for i in range(K)]  # k*d
res = 0

for i in range(n):
    fm[0][i] = arr[i]
    fn[0][i] = arr[i]

    """
定义fm[k][i]表示当选中了k个学生，并且以第i个学生为结尾，所产生的最大乘积；
        fn[k][i]表示 当选中了k个学生，并且以第i个学生为结尾，所产生的最小乘积；
那么fm[k+1][i+1]=max(fm[k][i]*stu[i+1],fn[k][i]*stu[i+1])，
        即当选中了k个学生后，再选择第i+1编号学生，所产生的最大乘积；
        然而，并不能保证上一次选择的就是第i个学生，所以要遍历子数组fm[k]，
        令j从i到1，并且j与i+1之间小于间隔D，遍历fm[k][j]，以及fn[k][j]；
同理fn[k+1][i+1]=min(fn[k][i]*stu[i+1],fm[k][i]*stu[i+1])。
最后，遍历一遍fm[K][i]求得最大值（i从1～N）。
    """

for i in range(n):
    for k in range(1, K):
        # for j in range(i-1,-1,-1):
        for j in range(i - 1, max(0, i - D) - 1, -1):
            # if (i-j<D and k>0):
            fm[k][i] = max(fm[k][i], max(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))
            fn[k][i] = min(fn[k][i], min(fm[k - 1][j] * arr[i], fn[k - 1][j] * arr[i]))

    res = max(res, fm[K - 1][i])

print(res)
```
