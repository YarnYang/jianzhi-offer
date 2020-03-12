# -*- coding:utf-8 -*-
'''
@题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

@解题思路
同样的，双指针思想，不同的是，在数组中，一个指针指向最右边，一个指向最左边，逐步往中间走，根据小学的知识我们知道，和确定的两个数，差越小乘积越大，因此用这种方法，找到的第一对数就是结果。

如果和大于S，右边的指针往左走一步，否则左边的指针往右走一步。
'''
class Solution:
	def FindNumbersWithSum(self, array, tsum):
		# write code here
		low = 0
		high = len(array) - 1
		while low < high:
			if array[low] + array[high] == tsum:
				return [array[low], array[high]]
			elif array[low] + array[high] > tsum:
				high -= 1
			else:
				low += 1
		return []