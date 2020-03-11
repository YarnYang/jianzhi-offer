# -*- coding:utf-8 -*-
'''
@题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

@解题思路
遍历，用字典存储统计结果
遍历，找到只出现一次的字符。

这里需要注意的是，字典是无序的，所以不能找到第一个，这里我用了一个list来存储字符出现的顺序，因此在第二次遍历的时候是根据list的顺序，而不是字典的key的顺序，就可以结果字典无序的问题。

另外，可以调用Python的count函数解决问题：
s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1
讨论区大神的代码，一行就可以解决。
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        pos = {}
        l = []
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic.update({s[i]: 1})
                pos.update({s[i]: i})
                l.append(s[i])
        for i in l:
            if dic[i] == 1:
                return pos[i]
        return -1