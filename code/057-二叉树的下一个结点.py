# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
'''
@题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

@解题思路
- 有右子树
返回的是右子树最左边的结点

- 没有右子树
1. 如果当前结点是父节点的左节点，直接返回父节点
2. 若否，重复步骤1，直到没有父节点或父节点没有左子树
'''
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return pNode
        # 有右孩子
        if pNode.right:
            next = pNode.right
            while next.left != None:
                next = next.left
            return next
        # 无右孩子
        while 1:
            if pNode.next == None or pNode.next.left == None:
                return None
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        
        
        
        