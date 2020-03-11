# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
@题目描述：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

@解题思路
先判断是否有环，用两个指针，指针p1每次走一步，指针p2每次走两步，如果指针p1和指针p2能相遇，则有环。否则，无环。

如果有环，则找到环的入口结点。我们设环的长度为m，表头到入口结点的长度为n，那么我们可以知道：
p2-p1 = m # p2能与p1相遇，说明p2比p1多走了一圈
p2走的步数 = 2*p1走的步数 #很明显，因为p2每次走两步，p1每次走一步
所以，p1走的步数=m，p2走的步数=2m

继续假设从入口结点到相遇的位置的步数为x，那么有m = x + n
我们要求的就是n的位置。那么，从相遇的位置到入口结点就是n，从表头到入门结点也是n，这部分具体的推导可以自己画个图，很容易理解。

于是我们只需要让p1从表头开始走，p2从相遇的地方开始走，两者再次相遇的位置就是入口结点。

以上的推导是基于m > n，在这种情况下p1,p2相遇p2只走了一圈，当m很小的时候，或许p2已经走了很多圈了，针对这种情况我也做了证明，是可以满足以上过程的，具体证明就不讲解了，其实思路是一样的。
'''
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 判断是否有环
        if pHead == None or pHead.next == None:
            return None
        p1 = pHead.next
        p2 = pHead.next.next
        while p1 != p2:
            if p2.next != None and p2.next.next != None:
                p1 = p1.next
                p2 = p2.next.next
            else:
                return None
        p2 = pHead
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        '''
        l = []
        while pHead:
            if pHead in l:
                return pHead
            l.append(pHead)
            pHead = pHead.next
        '''
        
            