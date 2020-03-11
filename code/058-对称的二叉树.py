# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

@解题思路
一颗对称的二叉树：
		 5
	   /  \
	  4	   4
	 / \  / \
	3  2  2  3
显然，root结点的左右子树应该相等，且左右子树应该成镜像关系，即左子树的左节点应该等于右子树的右节点。
'''
class Solution:
	def helper(self, left, right):
		if left == None or right == None:
			if left == None and right == None:
				return True
			else:
				return False
		# 首先判断左右子树的父节点是否相等
		if left.val != right.val:
			return False
		# 然后判断左右子树是否对称是判断左节点是否等于右节点
		else:
			return self.helper(left.left, right.right) and self.helper(left.right, right.left)

	def isSymmetrical(self, pRoot):
		# write code here
		if pRoot == None:
			return True
		# 只要有一个为None,就进入判断条件，两个都为None则返回True。否则返回False
		if pRoot.left == None or pRoot.right == None:
			if pRoot.left == pRoot.right:
				return True
			else:
				return False
		# 只有左右结点相等，才继续判断左右子树是否对称
		if pRoot.left.val == pRoot.right.val:
			return self.helper(pRoot.left, pRoot.right)
		else:
			return False