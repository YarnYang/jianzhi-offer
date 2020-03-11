# -*- coding:utf-8 -*-
# import queue
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def Permutation(self, ss):
		# write code here
		if len(ss) <= 1:
			return ss
		res = []
		length = len(ss)
		ss = list(ss)
		ss.sort()
		res.append(''.join(ss))
		while 1:
			p = length - 2
			# 找到第一个递减的数
			while p >= 0 and ss[p] >= ss[p + 1]:
				p -= 1
			# 说明已经没有递减的数了，break
			if p < 0:
				break
			q = length - 1
			# 找到后面数第一个比ss[p]大的数
			while ss[p] >= ss[q]:
				q -= 1
			ss = self.swap(ss, p, q)
			ss = self.reserve(ss, p+1)
			res.append(''.join(ss))
		return res

	def swap(self, ss, p, q):
		t = ss[p]
		ss[p] = ss[q]
		ss[q] = t
		return ss

	def reserve(self, ss, k):
		pre = ss[:k]
		ss = ss[k:]
		for i in range(int(len(ss) / 2)):
			ss = self.swap(ss, i, len(ss) - i - 1)
		pre.extend(ss)
		return pre




root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(8)
# root.right.right = TreeNode(8)
root.left.left.left = TreeNode(4)
# root = None

pHead = RandomListNode(1)
p = pHead
for i in range(2,6):
	p.next = RandomListNode(i)
	p = p.next
p = pHead
p.random = p.next.next.next
p = p.next.next
p.random = p.next.next

def print_tree(root):
	if root == None:
		return
	print(root.val)
	print_tree(root.left)
	print_tree(root.right)

def print_link(head):
	while head:
		if head.random != None:
			print(head.label, head.random.label)
		else:
			print(head.label)
		head = head.next

a = Solution()

s = 'baa'
# a.Insert(s)
print(a.Permutation(s))
# print(l)