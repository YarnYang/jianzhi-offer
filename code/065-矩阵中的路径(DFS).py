# -*- coding:utf-8 -*-
'''
@题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

@解题思路
这道题用深搜比较好，具体看实现吧。
'''
class Solution:
	def hasPath(self, matrix, rows, cols, path):
		# write code here
		if path == '':
			return True

		def dfs(x, y, p):
			# 若x,y越界，返回False
			if not (0<=x<rows and 0<=y<cols):
				return False
			# 若当前字符与p中的字符不相符，或当前格子已经走过了，返回False
			if matrix[x*cols+y] != p[0] or book[x][y] == 1:
				return False
			# 当前字符与p中的一个字符相等，标记当前格子为已走过
			book[x][y] = 1
			# 如果p的长度等于1了，说明路径可以找到，返回True
			if len(p) <= 1:
				return True
			# p的长度不为1，继续向四个方向寻找，注意此时p=[1:]
			return dfs(x, y+1, p[1:]) or dfs(x-1, y, p[1:]) or dfs(x, y-1, p[1:]) or dfs(x+1, y, p[1:])

		# 任何一个点都可以作为起点的位置
		for i in range(rows):
			for j in range(cols):
				# 不同的点作为起点的位置就是一次重新尝试，book数组要重置
				book = [[0] * cols for k in range(rows)]
				# 进行dfs
				if dfs(i, j, path): 
					return True
		return False