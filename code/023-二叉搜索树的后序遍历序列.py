# -*- coding:utf-8 -*-
'''
@题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

@解题思路
后序遍历：左节点 右节点 父节点

结合后序遍历和二叉搜索树的特点，数组最后一个数为根节点，比根节点小的都是左子树，比根节点的的是右子树。因此，判断是否是后序遍历的结果，就是判断能否根据root结点的值将数组分为小于root和大于root的两部分，可递归求解。
'''
class Solution:
	def isBST(self, sequence):
		# 递归结束的条件，只剩一个结点或0个结点
		if len(sequence) == 0 or len(sequence) == 1:
			return True
		# 根节点的值
		root = sequence[-1]
		i = 0
		# 小于根节点的值，获取index，即sequence[:index]都小于root，即为左子树
		while root > sequence[i]:
			i += 1
		index = i
		# 左子树之外的就是右子树，sequence[index:]，理论上右子树的值都要比root大，否则返回False
		for i in sequence[index:]:
			if root > i:
				return False
		# 递归判断左右子树是否满足条件
		return self.isBST(sequence[:index]) and self.isBST(sequence[index:-1])

	def VerifySquenceOfBST(self, sequence):
		# write code here
		if len(sequence) == 0:
			return False
		if len(sequence) == 1:
			return True

		return self.isBST(sequence)


