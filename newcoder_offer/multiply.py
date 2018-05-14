# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。


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
