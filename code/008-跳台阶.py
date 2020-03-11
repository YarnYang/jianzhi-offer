# -*- coding:utf-8 -*-
'''
@题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

@解题思路
这种题先找规律
1：1
2：2
3：3
4：5
5：8
列了5个之后结果就差不多出来了，就是fibonacci数列。因此解法与007相同。
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 2
        for i in range(number - 2):
            b = a + b
            a = b - a 
        return b