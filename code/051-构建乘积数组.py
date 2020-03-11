# -*- coding:utf-8 -*-
'''
@题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

@解题思路
再构造两个数组，B，C
B[i] = A[0] * A[1] * ... * A[i-1]
C[i] = A[i+1] * A[i+2] * ... * A[n]

最终的结果就是
B[i] = B[i] * C[i]
'''
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [A[i] for i in range(n)]
        B[0] = 1
        for i in range(1, n):
            B[i] = A[i-1] * B[i-1]
        C = [A[-1] for i in range(n)]
        C[-1] = 1
        for i in range(1, n):
            C[n-i-1] = C[n-i] * A[n-i]
        for i in range(n):
            B[i] *= C[i]
        return B
        