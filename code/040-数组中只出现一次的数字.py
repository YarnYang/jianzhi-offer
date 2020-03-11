# -*- coding:utf-8 -*-
'''
@题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

@解题思路
HashMap：直接遍历，用字典进行统计出现的次数，然后重新遍历字典，只出现一次就加入到list。

看了讨论区，用位运算的方法，很巧妙，在此说一下思路，具体就不实现了。

两个相同的数字异或的结果一定为0，因此将这个数组中全部数字都进行异或，得到的结果肯定就是那两个只出现一次的数字的异或结果。

根据异或结果最低位为1，将所有数字分为两部分，如最后异或结果最低位为1的是倒数第二位，那就根据所有数字倒数第二位是不是1将数组分为两类，显然我们就能将出现一次的数字分到这两类中，两类各自相与的结果就是答案。

'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic = {} #用于统计数组出现的次数
        res = [] #返回结果
        # 遍历，统计出现次数
        for i in range(len(array)):
            if array[i] in dic:
                dic[array[i]] += 1
            else:
                dic.update({array[i]: 1})
        # 遍历dic，找到只出现一次的数字
        for i in list(dic.keys()):
            if dic[i] == 1:
                res.append(i)
                if len(res) == 2:
                    return res