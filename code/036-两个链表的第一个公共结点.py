# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述
输入两个链表，找出它们的第一个公共结点。

@解题思路
公共节点，后面所有的结点都相等，因此公共结点后链表的长度也相等。
根据这个思路，只需要统计链表的长度，然后舍弃长链表前面的结点直到与短链表一样长，此时再逐一判断当前结点是否相同。相同就是第一个公共结点。
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = 0
        len2 = 0
        p1 = pHead1
        p2 = pHead2
        # 获取两条链表的长度
        while pHead1 != None:
            len1 += 1
            pHead1 = pHead1.next
        while pHead2 != None:
            len2 += 1
            pHead2 = pHead2.next
            
        if len1 < len2:
            p1, p2 = p2, p1 #长链表为p1，短链表为p2
        # 舍弃长链表前面的结点
        for i in range(abs(len1 - len2)):
            p1 = p1.next
        # 判断是否相同
        while p1 != p2:
                p1 = p1.next
                p2 = p2.next
        return p1
    
    
