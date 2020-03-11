# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

@解题思路
很简单，用栈遍历结点就好啦。

下面的解法用了两个栈的原因在于要求每一层输出一行，那么用一个栈来表示当前层，一个栈用来存下一层的结点，当前层遍历完就使下一层等于当前层，循环上述过程，直到下一层没有新的结点入栈。
'''
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        s = [pRoot]
        result_all = []
        while s != []:
            s1 = []
            result = []
            while 1:
                now = s.pop(0)
                result.append(now.val)
                if now.left != None:
                    s1.append(now.left)
                if now.right != None:
                    s1.append(now.right)
                if s == []:
                    s = s1
                    break
            result_all.append(result)
        return result_all