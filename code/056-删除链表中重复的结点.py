# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
@题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

@解题思路
原本的解题思路为先遍历一次，找到重复结点的值存入list，再遍历一次，如果这个值是重复结点那就跳过，这种解题思路在1->2->3->2->3->4的时候也可以应对，结果将为1->4。也就是重复结点不连续时也可以处理。

但是看讨论区的答案，重复结点好像都是连续的，所以用一种新的解题思路。

两个指针，pre指向确定不重复的结点，now指向下一个结点，如果now和now的下一个结点相同的话，就跳过这两个结点，具体实现看代码。

有一个很巧妙的处理，如果第一第二个结点是重复结点将会很难处理，我们可以通过构造一个结点加到表头来使这种情况变得更容易处理，处理方法就和后面一样。
'''
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 构造一个结点放在表头，用于更好地应对第一第二个结点相同的情况
        head = ListNode(0)
        head.next = pHead
        pre = head
        while pre.next:
            now = pre.next
            if now.next != None and now.val == now.next.val:
                while now.next != None and now.val == now.next.val:
                    now = now.next
                pre.next = now.next
            else:
                pre = pre.next
        return head.next
        # if pHead == None or pHead.next == None:
        #     return pHead
        # l = []
        # l_repeat = []
        # p = pHead
        # while p != None:
        #     if p.val in l:
        #         l_repeat.append(p.val)
        #     l.append(p.val)
        #     p = p.next
        # while pHead != None and pHead.val in l_repeat:
        #     pHead = pHead.next
        # if pHead == None:
        #     return None
        # head = pHead
        # a = pHead
        # p = pHead.next
        # while p != None:
        #     if p.val not in l_repeat:
        #         a.next = p
        #         a = a.next
        #     p = p.next
        # a.next = None
        # return head
        