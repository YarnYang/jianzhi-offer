# -*- coding:utf-8 -*-
'''
@题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

@解题思路
暴力的方法当然还是使用字典统计，但是讨论区有更好的方法：
遍历一次数组，在遍历的过程中比较array[i]和array[i-1]是否相同，若相同count++，若不相同count--，若count==0，则将num中的数替换为当前数。如果存在这样的数，剩下的那个num就是要求的数，因此遍历一遍判断是否超过数组长度的一半。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        num = numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i] != num:
                count -= 1
                if count == 0:
                    num = numbers[i]
                    count = 1
            else:
                count += 1
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == num:
                count += 1
        if count > len(numbers) / 2:
            return num
        return 0