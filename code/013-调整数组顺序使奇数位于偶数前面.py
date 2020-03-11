# -*- coding:utf-8 -*-
'''
@题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

@解题思路
看了讨论区各种插入排序什么的，搞了半天时间复杂度也就是O(n)甚至更高，不如直接遍历一下不好吗？

尝试过快排的思想一个从左找偶数一个从右找奇数互换，但是这题的要求需要相对位置不变，因此也不合适，还是遍历吧。

开两个list，一个放奇数一个放偶数，最后合并，简单有效。
'''
class Solution:
    def reOrderArray(self, array):
        i = 0
        res_odd = []
        res_even = []
        while i < len(array):
            if array[i] % 2 == 1: #奇数
                res_odd.append(array[i])
            else: #偶数
                res_even.append(array[i])
            i += 1
        res_odd.extend(res_even)
        return res_odd