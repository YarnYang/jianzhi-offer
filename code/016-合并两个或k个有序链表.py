# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

@解题思路
合并的过程其实就是归并排序的思想，判断两个链表当前的值，把小的放入到新建的链表中。
'''
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        # 用于标记是否已创建头结点
        f = 1
        # 两个都不为None，循环
        while pHead1 != None and pHead2 != None:
            if pHead1.val <= pHead2.val:  #更小的那个值添加到新的链表中
                a = pHead1
                pHead1 = pHead1.next
            else:
                a = pHead2
                pHead2 = pHead2.next
            if f:
                head = a
                b = a
                f = 0
            b.next = a 
            b = a
        # 把非空的链表加入到新建链表的链尾，return head
        if pHead1 == None:
            b.next = pHead2
            return head
        elif pHead2 == None:
            b.next = pHead1
            return head
            
                
                