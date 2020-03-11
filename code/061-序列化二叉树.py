# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

@解题思路
把二叉树按层序遍历序列化，很简单，结点结束+！，空节点为#

反序列化，按队列存储非空结点，层序还原二叉树
'''
class Solution:
    # 层序遍历
	def Serialize(self, root):
		# write code here
		if root == None:
			return ''
		s = str(root.val) + '!'
		q = []
		q.append(root)
		while q:
			now = q.pop(0)
			if now.left:
				q.append(now.left)
				s = s + str(now.left.val) + '!'
			else:
				s += '#'
			if now.right:
				q.append(now.right)
				s = s + str(now.right.val) + '!'
			else:
				s += '#'
		return s

	def Deserialize(self, s):
		if s == '':
			return None
		q = []
		i = 0
		while s[i] != '!':
			i += 1
		root = TreeNode(int(s[:i]))
		q.append(root)
		s = s[i+1:]
		while s:
			i = 0
			now = q.pop(0)
			for j in range(2):
				i = 0
				while s[i] != '!' and s[i] != '#':
					i += 1
				if s[i] == '!':
					if j == 0:
						now.left = TreeNode(int(s[:i]))
						q.append(now.left)
					else:
						now.right = TreeNode(int(s[:i]))
						q.append(now.right)
				else:
					if j == 0:
						now.left = None
					else:
						now.right = None
				s = s[i+1:]

		return root