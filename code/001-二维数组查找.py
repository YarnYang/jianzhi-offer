# -*- coding:utf-8 -*-
'''
@题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

@解题思路
从数组的左下角开始，往上递减，往右递增，因此只需判断target与当前的数相比较，相等则返回True，若target>array[i]，向右移动，否则向上移动，直到超出数组边界停止，返回False。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        move = [[0,1], [-1,0]] #右移，上移
        x = len(array) - 1
        y = 0
        
        while x>=0 and y<len(array[0]):
            if target == array[x][y]:
                return True
            if target > array[x][y]:
                x = x + move[0][0]
                y = y + move[0][1]
            else:
                x = x + move[1][0]
                y = y + move[1][1]
        return False