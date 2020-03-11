# -*- coding:utf-8 -*-
'''
@题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

@解题思路
利用Python的split函数将字符串分为word，然后用队列的思想将word pop出去即可。
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        list_s = s.split(' ')
        res = []
        for i in range(len(list_s)):
            res.append(list_s.pop())
        return " ".join(res)
        '''
        l = []
        last = len(s)
        last_space = len(s)
        for i in range(len(s)):
            if s[-i] == ' ':
                last_space = len(s) - i
                l.extend(s[-i + 1:last])
                l.append(' ')
                last = len(s) - i
        l.extend(s[:last_space])
        return ''.join(l)
        '''