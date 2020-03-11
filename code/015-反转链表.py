# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述：
输入一个链表，反转链表后，输出新链表的表头。

@解题思路
一遍遍历链表，一遍新建链表就可以了。
因为是翻转链表，需要储存上一个结点，然后当前结点的next=上一个结点，最后返回当前结点就是表头
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return
        # b是上一个结点，初始化为None
        b = None
        while 1:
            # a是当前结点
            a = ListNode(pHead.val)
            a.next = b
            pHead = pHead.next
            # 遍历完成，返回当前结点即表头
            if pHead == None:
                return a
            b = a
            