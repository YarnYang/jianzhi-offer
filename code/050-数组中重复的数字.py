# -*- coding:utf-8 -*-
'''
@题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

@解题思路
由于知道数字的范围，那么可以直接用一个book数组来标记数字是否出现过，若出现过直接返回当前数字即可。
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        # 初始化book数组都为0
        book = [0 for i in range(len(numbers))]
        # 遍历numbers中的数字
        for i in range(len(numbers)):
            # 若没有出现过，则标记为1
            if book[numbers[i]] == 0: 
                book[numbers[i]] = 1
            # 若出现过，直接存到duplication[0]中，返回
            else:
                duplication[0] = numbers[i]
                return True
        return False