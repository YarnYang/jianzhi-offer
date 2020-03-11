# -*- coding:utf-8 -*-
'''
@题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

@解题思路
由于是连续序列，只要设置两个指针，一个在前一个在后，计算两个指针之间的和，若小于100，右边指针走一步，大于100，左边指针走一步。
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        low = 1
        high = 2
        while low < high:
            sum_ = (low + high) * (high - low + 1) / 2
            if sum_ == tsum:
                tres = []
                for i in range(low, high+1):
                    tres.append(i)
                res.append(tres)
            if sum_ < tsum:
                high += 1
            else:
                low += 1
        return res