# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
'''
@题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

@解题思路
看完讨论区突然发现自己的解法不对...可太难受了哈哈哈。说一下原来的解法，第一次遍历，新建一条链表与原链表相同，此时没有random结点。第二次遍历，将random结点加上。但是这里的问题就是，用我这种方法，复制后的链表random结点是指向原链表的。

说一下正确的思路：
1.在原链表的基础上复制结点，也就是原链表是A-B-C-D, 复制之后为A-A'-B-B'-C-C'-D-D'，也就是在原结点的后面复制一个结点，之所以要在同一条链上复制，就是为了可以快速找到rondom结点的位置。
2.找到复制结点的random结点
3.拆分两条链表。拆分方法也很简单，中间隔一个结点重新成链就好了。
'''
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return pHead
        # 复制结点
        now = pHead
        while now != None:
            clone = RandomListNode(now.label)
            clone.next = now.next
            now.next = clone
            now = clone.next
        # 复制Rondom结点
        now = pHead
        while now != None:
            if now.random:
                now.next.random = now.random.next
            now = now.next.next
        # 拆分链表
        clonehead = clone = pHead.next
        now = pHead
        while now != None:
            now.next = clone.next
            now = now.next
            clone.next = now.next if now else None
            clone = clone.next
        return clonehead