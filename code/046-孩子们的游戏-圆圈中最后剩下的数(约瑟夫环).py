# -*- coding:utf-8 -*-
'''
@题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

如果没有小朋友，请返回-1

@解题思路
约瑟夫环的问题，原来的方法是直接模拟了这个过程，相当于把list当做链表来处理，但是时间复杂度较高，考虑用约瑟夫环的方法来做。

https://blog.csdn.net/u011500062/article/details/72855826
这篇文章对约瑟夫环讲解的非常详细，推荐。

约瑟夫环的递推公式：
f(n, m) = (f(n-1, m) + m) % n
解释一下这个公式的意思，首先f(n, m)，n表示有n个人，m表示指定的数，因此f(n-1,m)就是有n-1个人，m仍为指定的数。f(n,m)表示的意思是最后一个人的编号。那么如果知道f(n-1,m)的编号，就可以通过f(n-1, m) + m 来找到第n个人的编号，由于+m可能溢出，因此%n。

很容易知道f(1, m) = 0，因为只有一个人，编号一定为0
'''
class Solution:
	def LastRemaining_Solution(self, n, m):
		# write code here
        if n == 0:
            return -1
        num = 0
        for i in range(n-1):
            num = (num + m) % (i+2)
        return num
		# if n == 0:
		# 	return -1
		# stu = [i for i in range(n)]
		# mod = 0
		# while len(stu) > 1:
		# 	mod = (mod + m -1) % len(stu)
		# 	stu.pop(mod)
		# return stu[0]