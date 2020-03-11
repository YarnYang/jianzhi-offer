# -*- coding:utf-8 -*-
'''
@题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

@解题思路
递归求解很快就报超时，因此直接自底向上求解
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a = b = 1
        for i in range(n-2):
            b = a + b
            a = b - a
        return b