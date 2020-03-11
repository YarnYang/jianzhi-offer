# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述
输入一个链表，输出该链表中倒数第k个结点。

@解题思路
要知道倒数第k个，而链表只有从前面到后面的链接，因此还是需要全部都遍历一遍放到数组中然后取出倒数第k个。
'''
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head is not None:
            l.append(head)
            head = head.next
        #主要判断若k大于链表长度或等于0，都返回None
        if len(l) < k or k==0:
            return 
        return l[len(l) -k]