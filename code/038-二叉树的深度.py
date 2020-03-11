# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

@解题思路
根节点深度为1，取max(左子树深度，右子树深度)+1就是树的深度。
'''
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        return max(1 + self.TreeDepth(pRoot.left), 1 + self.TreeDepth(pRoot.right))
   