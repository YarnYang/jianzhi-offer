# -*- coding:utf-8 -*-
'''
@题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

@解题思路
找到最小的前k个数，最合理的当然是使用最小堆的方法，但是最小堆最好的情况是已经有最小堆存在的情况下，只需要O(klogn)的时间复杂度，但是在没有最小堆的情况下，还需要建树，需要O(nlogn)的时间，其实不如直接排序取前n个。

排序可以用快排，归并排序等方法，下面使用的是最小堆的解法。包括建树，pop，insert等函数。
'''
class Solution:
	def GetLeastNumbers_Solution(self, tinput, k):
		# write code here,最小堆
		def parent(index):
			return int((index - 1) / 2)

		def left(index):
			return 2 * index + 1

		def right(index):
			return 2 * index + 2

		def swap(i1, i2):
			t = heap[i1]
			heap[i1] = heap[i2]
			heap[i2] = t

		def shift_up(index):
			while parent(index) >= 0 and heap[index] < heap[parent(index)]:
				swap(index, parent(index))
				index = parent(index)

		def shift_down(index):
			while 1:
				# 左右结点中值更小的用于交换
				if left(index) < len(heap):
					swap_index = left(index) if right(index) >= len(heap) or heap[left(index)] < heap[right(index)] else right(index)
					if heap[index] > heap[swap_index]:
						swap(index, swap_index)
						index = swap_index
					else:
						break
				else:
					break

		def insert(num):
			heap.append(num)
			if len(heap) > 1:
				index = len(heap) - 1
				shift_up(index)

		def pop():
			top = heap[0]
			now = heap.pop()
			if len(heap) > 0:
				heap[0] = now
				shift_down(0)
			return top

		def build_heap():
			for i in range(len(tinput)):
				insert(tinput[i])
		if k > len(tinput):
			return []
		heap = []
		build_heap()
		res = []
		for i in range(k if k <= len(tinput) else len(tinput)):
			res.append(pop())
		return res
