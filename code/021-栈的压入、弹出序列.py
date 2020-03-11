# -*- coding:utf-8 -*-
'''
@题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

@解题思路
每压入一个数字，判断当前压入数字与当前弹出数字是否相等，若不相等则继续压入；若相等则弹出，并判断上一个压入的数字是否为当前要弹出的数字，是的话继续弹出，循环。

需要用一个list来存储已经压入的数，pushV和popV的下标都只能向前走，如果想得到之前push进来的数查看list数组。

文字表述可能没那么清晰，继续见代码。
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        i, j = 0, 0 #i，j用来表示push和pop的数组下标
        l = [] 
        # 若pop的下标j大于等于pop的长度，说明popV数组已经全部被遍历过了，返回True
        while j < len(popV):
            #如果当前值相等，i，j都向前走一步
            if i < len(pushV) and pushV[i] == popV[j]: 
                j += 1
                i += 1
            # 如果当前值不相等
            else:
                # 判断最近入栈的值与当前出栈的值是否相等，若是list中的数pop表示出栈，j+1表示出栈
                if l != [] and l[-1] == popV[j]:
                    l.pop()
                    j += 1
                # 如果i已经大于pushV的长度了，说明pushV已经遍历完了，但是不满足出栈条件，返回False
                elif i >= len(pushV):
                    return False
                # 当前push值和pop不相等，上一个push值和pop也不相等，那就把当前值push进list
                else:
                    l.append(pushV[i])
                    i += 1
        return True
            