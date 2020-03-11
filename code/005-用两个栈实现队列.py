# -*- coding:utf-8 -*-
'''
@题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

@解题思路
栈：先进后出，后进先出
队列：先进先出

对于1，2，3，4，5这列数字，入栈s1(1,2,3,4,5)，从s1入栈s2，s1的出栈顺序为5,4,3,2,1，因此得到的栈s2(5,4,3,2,1)，栈s2的出栈顺序为1,2,3,4,5，也就是队列的出列顺序。因此可以用两个栈实现一个队列。

具体的做法为，判断s2是否为空，不为空直接出栈，若空，将s1中的数据入栈到s2，s2出栈。
'''
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        # write code here
        self.s1.append(node)
    def pop(self):
        # return xx
        if len(self.s2) == 0: # 若s2为空，将s1数据全部出栈到s2
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        a = self.s2.pop()
        return a