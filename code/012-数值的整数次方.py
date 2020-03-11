# -*- coding:utf-8 -*-
'''
@题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
'''
import math
class Solution:
    def Power(self, base, exponent):
        # write code here
        #return base**exponent #用python可一行解决
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        pro = 1
        for i in range(abs(exponent)):
            pro *= base
        if exponent > 0:
            return pro
        else:
            return float(1/pro)
        