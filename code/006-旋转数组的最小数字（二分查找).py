# -*- coding:utf-8 -*-
'''
@题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

@解题思路
暴力解法当然就是遍历，但是我们选择更好的解法，二分查找。

首先，二分查找是对于有序数组来说，若查找的数等于中间的数，那么返回，若小于，往左边找，否则往后边找。

这题是一个旋转有序数组，也就是将数组分为两个部分，都是递增的，但是左边的数都大于右边的数，中间的数就是最小值。

类似的查找思路，判断mid是否是最小值，若是，返回，若不是：
跟最右边的数比，因为最右边的数是左半边中最小的，右半边中最大的。因此mid < right，应该在左边找，否则就在右边找。

另外需要注意的是，如何判断是都为最小值，因为允许有相同的数，因此要找左右两边与当前mid不相同的数进行比较，也就是5 6 1 2 2 2 3 4，若当前mid是第二个2，那我们应该找到左边的1和右边的3进行比较。

'''
class Solution:
	def minNumberInRotateArray(self, rotateArray):
		# write code here
		return self.find_min(rotateArray, 0, len(rotateArray) - 1)

	def if_min(self, array, mid):
		left = right = mid
		# 一直往左边找直到找到不同的数，且不能越界
		while array[left] == array[mid] and left > 0:
			left -= 1
		# 一直往右边找知道找到不同的书，且不能越界
		while array[right] == array[mid] and right < len(array) - 1:
			right += 1
		# 比两边的数都小则为最小值
		if array[mid] <= array[left] and array[mid] <= array[right]:
			return True
		return False

	def find_min(self, array, left, right):
		mid = int((left + right) / 2)
		if self.if_min(array, mid):
			return array[mid]
		# 跟最右边的数比，因为最右边的数是左半边中最小的，右半边中最大的。
		# 因此mid < right，应该在左边找，否则就在右边找
		if array[right] <= array[mid]:
			return self.find_min(array, mid + 1, right)
		# 否则往左边找
		else:
			return self.find_min(array, left, mid - 1)