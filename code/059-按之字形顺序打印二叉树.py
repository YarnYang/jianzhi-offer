# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

@解题思路
1. 用栈存结点
2. 结点的存入顺序为: 奇数行先存左结点，再存右节点；偶数行相反
3. 需要两个栈，一个用于存这一层的结点，一个用于存下一层的结点

看一个例子：
		 5
	   /  \
	  3	   8
	 / \  / \
	2  4  7  9
正确的打印顺序为：
5, 8，3，2，4，7，9

1.将5入栈[5]
2.5出栈，打印，由于在第一层奇数层，先存左节点，存入另一个栈中[3,8]
3.8出栈，打印，偶数层，先存右节点，存入另一个栈[9，7]; 3出栈，打印，同样先存右节点[9，7，4，2]
4. [9,7,4,2]依次出栈，打印顺序为，2，4，7，9.

与正确打印顺序相同。
'''
class Solution:
	def Print(self, pRoot):
		# write code here
		if pRoot == None:
			return []
		flag = 1 # 用于判断是奇数层还是偶数层，1为奇数层，-1为偶数层
		s = [] # 栈，用于记录当前层的结点
		result_all = [] #用于保存所有结果
		s.append(pRoot)
		while s != []:
			s1 = [] # 栈，用于记录下一层的结点
			result = [] #用于保存当前层打印的结点
			while s != [] 
				now = s.pop()
				result.append(now.val)
				if flag == 1: # 如果是奇数层，先存左节点，再存右节点
					if now.left != None:
						s1.append(now.left)
					if now.right != None:
						s1.append(now.right)
				else: # 否则，偶数层，先存右节点，再存左节点
					if now.right != None:
						s1.append(now.right)
					if now.left != None:
						s1.append(now.left)
			flag *= -1 # 改变下一层的奇偶性
			s = s1 # 把下一层的栈赋给当前层
			result_all.append(result)
		return result_all