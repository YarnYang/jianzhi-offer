# -*- coding:utf-8 -*-
'''
@题目描述
统计一个数字在排序数组中出现的次数。

@解题思路
首先找到这个数，用二分查找的方法。
找到之后再统计左右两边是否有相等的数，统计次数。
'''
class Solution:
	def GetNumberOfK(self, data, k):
		# write code here
		return self.count_num(data, 0, len(data) - 1, k)


	def count_num(self, data, left, right, k):
		mid = int((left + right) / 2)
		if left > right:
			return 0
		if data[mid] == k:
			count = 1
			l = mid - 1
			r = mid + 1
			while l >= 0 and data[l] == k:
				count += 1
				l -= 1
			while r < len(data) and data[r] == k:
				count += 1
				r += 1
			return count
		if k < data[mid]:
			return self.count_num(data, left, mid - 1, k)
		else:
			return self.count_num(data, mid + 1, right, k)