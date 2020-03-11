# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

@解题思路
判断二叉树是否为平衡二叉树就是判断左右子树的高度差是否超过1，超过1就不是平衡二叉树。计算高度的方法就是，1 + max(left, right)。

递归求解。
'''
class Solution:
    def get_depth(self, root):
        if root == None:
            return 0
        # 计算左右子树的高度
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        # 任一左右子树高度差超过1都会返回-1，那就不是平衡二叉树
        if right == -1 or left == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right) # 计算树的高度
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return (self.get_depth(pRoot) != -1)