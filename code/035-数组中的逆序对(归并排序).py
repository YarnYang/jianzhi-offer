'''
@题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

@解题思路
归并排序的变形，其实就是统计某个数字前面有几个比它大的数字，那么联系归并排序的过程，就是统计A，B在归并的过程中，把B中的数字放入归并的数组时，A中元素的个数，将所有的统计过程进行累加，就是结果。 

其中，把B中的数字放入归并的数组，其实就是A中的数字比B中的大，而A中的数字又排在B前面，所以此时A的长度就是逆序对的数量。
'''
class Solution:
	def InversePairs(self, data):
		self.count = 0 #逆序对的数量
		# 归并排序
		def merge_sort(lists):
			if len(lists) <= 1:
				return lists
			mid = int((0 + len(lists)) / 2)
			left = merge_sort(lists[:mid]) #把数组分为左右两个部分分别进行归并
			right = merge_sort(lists[mid:])
			l, r = 0, 0
			res = []
			# 合并left和right两个数组，合并的结果存在res中
			while l < len(left) and r < len(right):
				# 如果left小于right，那直接加入到res中
				if left[l] <= right[r]: 
					res.append(left[l])
					l += 1
				# 若right小于left，把right加入到res中，同时count加上此时left中元素的个数
				else:
					res.append(right[r])
					r += 1
					self.count += len(left) - l
			# 把left或者right剩余的数加入到res
			res.extend(left[l:])
			res.extend(right[r:])
			return res

		merge_sort(data)
		return self.count % 1000000007
            