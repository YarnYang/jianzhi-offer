# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

@解题思路
遍历链表，把结点值存入list，从尾到头打印，使用l[::-1]
'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        if listNode is None:
            return l
        while listNode.next is not None:
            l.append(listNode.val)
            listNode = listNode.next
        l.append(listNode.val)
        return l[::-1]
    
    