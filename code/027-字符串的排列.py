# -*- coding:utf-8 -*-
'''
@题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

@解题思路
原答案用了python的递归求解方法，用了set直接去重，不推荐。

经典的全排列有两种解法，递归法和字典序的方法，由于字典序的方法可以保持从小到大的排列，因此本题采用字典序。

简单讲一下字典序的思路，具体的可以看博客：
https://blog.csdn.net/lemon_tree12138/article/details/50986990

以3 4 6 9 8 7 5 2 1为例：
1. 从右向左找到第一个递减的数，例子中就是6，因为9到6是递减
2. 重新从右到左找到第一个比6大的数，在例子中是7
3. 交换6，7的位置，数列变为3 4 7 9 8 6 5 2 1，可以看到7之后的数是递减的数列
4. 将7之后的数逆序，得到3 4 7 1 2 5 6 8 9就是下一个排列。

代码实现中的几个细节：
1.首先要对原序列中的字符排序，使其从小到大排列。
2.字典序的方法可以很好地应对字母相同的情况，因此上述步骤1，2中若碰到相等的应该继续寻找不停留
'''
class Solution:
    def Permutation(self, ss):
		# write code here
		if len(ss) <= 1:
			return ss
		res = []
		length = len(ss)
		ss = list(ss) # 将字符串转为list并排序，转为list的目的就是排序
		ss.sort()
		res.append(''.join(ss)) #把排序号的加入到结果中
		# 开始查找字典序的排列
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
			ss = self.swap(ss, p, q) # 交换
			ss = self.reserve(ss, p+1) #找到逆
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

        # if len(ss) <= 1:
        #     return ss
        # res = set()
        # for i in range(len(ss)):
        #     for j in self.Permutation(ss[:i] + ss[i+1:]):
        #         res.add(ss[i] + j)
        # return sorted(res)
                