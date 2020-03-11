# -*- coding:utf-8 -*-
'''
@题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

@解题思路
用字典来统计出现过的次数，用list来记录字符出现的次数。
'''
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
    def FirstAppearingOnce(self):
        # write code here
        s_dic = {}
        l = []
        for i in range(len(self.s)):
            if self.s[i] in s_dic:
                s_dic[self.s[i]] += 1
            else:
                s_dic.update({self.s[i]: 1})
                l.append(self.s[i])
        for i in l:
            if s_dic[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char