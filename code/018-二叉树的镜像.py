# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。

@解题思路
二叉树的镜像定义：源二叉树 
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
二叉树的镜像就是左右结点互换。因此写一个递归实现，递归停止条件就是结点为None。
'''
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        head = root
        self.change(root)
        return head
        
    def change(self, root):
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        self.change(root.left)
        self.change(root.right)