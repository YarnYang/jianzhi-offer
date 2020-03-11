# -*- coding:utf-8 -*-
'''
@题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

@解题思路
返回最小值的时间复杂度为O(1)，因此一定是一直更新最小值，需要的时候直接返回。

首先要明确一点，我们保存的min应该是个list而不是一个变量，因为若你pop出当前的min，需要重新更新min，那就需要重新遍历一次栈，时间复杂度太高，我们可以将第二小的，第三小的都保存在list中，当最小的pop出之后，第二小的就是最小的，可以马上更新，复杂度为O(1).

主要是poo和push的时候需要注意。

具体看代码。
'''
class Solution:
	def __init__(self):
		self.l = [] #栈
		self.m = [] #用于保存min

	def push(self, node):
		# write code here
		self.l.append(node)
		if self.m == [] or self.m[-1] > node: #如果当前值为空，或者比当前最小值小，加入到min的list中
			self.m.append(node) 

	def pop(self):
		# write code here
		node = self.l.pop() 
		if node == self.m[-1]: #如果当前pop出的值是最小值，m中的值也需要pop出去。
			self.m.pop()
		return node

	def top(self):
		# write code here
		return self.l[0] if len(self.l) > 0 else None

	def min(self):
		# write code here
		return self.m[-1]