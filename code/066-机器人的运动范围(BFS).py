# -*- coding:utf-8 -*-
'''
@题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

@解题思路
思路比较简单，用BFS遍历即可，写了一个sum_helper函数用于计算行列坐标位数之和。

具体实现看代码吧。
'''
class Solution:
	# 定义了一种数据结构用于存储行列坐标
	class pos:
		def __init__(self, x, y):
			self.x = x
			self.y = y

	def movingCount(self, threshold, rows, cols):
		# write code here
		if threshold < 0:
			return 0
		book = [[0] * cols for k in range(rows)] # 用book数组标记为是否走过，初始化为0
		dire = [[0, -1, 0, 1], [1, 0, -1, 0]]  # 四个方向
		q = [] #用一个队列保存走过的格子
		q.append(self.pos(0, 0)) # 把第一个格子存入队列
		book[0][0] = 1 
		step = 1 #用于统计走过的格子数

		# 循环直到队列为空
		while len(q) > 0:
			now = q.pop(0)
			# 对四个方向进行循环
			for i in range(4):
				nx = now.x + dire[0][i]
				ny = now.y + dire[1][i]
				# 如果不越界且未遍历过，进入条件语句
				if 0 <= nx < rows and 0 <= ny < cols and book[nx][ny] == 0:
					book[nx][ny] = 1 #标记为已遍历
					# 行列坐标位数之和小于阈值，机器人才能到达格子
					if self.get_sum(nx, ny) <= threshold:
						q.append(self.pos(nx, ny))
						step += 1
		return step

	def get_sum(self, x, y):
		'''计算行列坐标位数之和'''
		return self.get_sum_help(x) + self.get_sum_help(y)

	def get_sum_help(self, num):
		'''计算一个数的位数坐标和'''
		sum = 0
		while num >= 10:
			sum += num % 10
			num = int(num / 10)
		return sum + num