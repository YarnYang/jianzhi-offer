# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

@解题思路
递归的方法，中序遍历二叉树的结果，其实就是一个排序数组，返回第k个结点即可。
'''
class Solution:
    # 返回对应节点TreeNode
    '''
    递归的方法，但是没有剪枝，而是遍历了所有的结点
    若剪枝，可以在mid上添加判断语句来进行剪枝
    '''
    def KthNode(self, pRoot, k):
        self.res = []
        self.mid(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def mid(self, p):
        if p == None:
            return p
        self.mid(p.left)
        self.res.append(p)
        self.mid(p.right)
    '''
    # 非递归的方法
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0 or pRoot == None:
            return None
        l = []
        p = pRoot
        while p != None:
            l.append(p)
            p = p.left
        while k != 0:
            if l == []: #若k的数量大于数中的结点数，返回None
                return None
            now = l.pop()
            k -= 1
            result = now
            if now.right != None:
                p = now.right
                while p != None:
                    l.append(p)
                    p = p.left
        return result
        '''  