# -*- coding:utf-8 -*-
'''
@题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

@解题思路
相当于重载比较符，如何比较呢，以32和321为例：
x = '32'
y = '321'
x + y > y + x则说明x大，否则y大。
'32321' > '32132' 因此x比y大。
再次比较3和321
y = '321'
z = '3'
'3213' < '3321' 因此z比y大。
比较3和32：
'332' > '323' 因此z比x大
即{3, 32, 321}的排序顺序应该为:
y < x < z
则最小的数组为:
321323

python对sort函数运算符的重载相当巧妙，可以好好学习。
'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        #先将数字转为str，存入list
        nums = list(map(str,numbers))
        # 进行比较，需要重载cmp，只有python2允许，Python3已经删去了cmp参数
        nums.sort(cmp = lambda x, y: cmp(x+y, y+x))
        # 将list合并为str，如果前面全是0的话去掉
        return ''.join(nums).lstrip('0')