# -*- coding:utf-8 -*-
'''
@题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

@解题思路
同样的，先找规律
2*1：1
2*2：2
2*3：3
2*4：5
2*5：8
同样的是个fibonacci数列的求解问题。
'''
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 1 or number == 0 or number == 2:
            return number
        a = 1
        b = 2
        for i in range(number - 2):
            b = a + b
            a = b - a 
        return b