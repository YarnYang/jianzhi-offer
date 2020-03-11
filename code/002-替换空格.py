# -*- coding:utf-8 -*-
'''
@题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

@解题思路
使用python的库函数偷懒了哈哈哈
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = s.split(" ") #按空格将字符串划分并存入list
        return "%20".join(l) #用"%20"将list中的字符相连接并返回字符串