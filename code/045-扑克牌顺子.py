# -*- coding:utf-8 -*-
'''
@题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大、小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

@解题思路
输入的是0 1 2 3之类的数字，其中0可以变成任何其他的数，那么我们先统计0的个数，剩下的数使其连成一个数字，在连成顺子的过程中，若缺少一个数则用0代替，若没有0了，则不能连成顺子。

思路很简单，具体实现看代码。
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        count_0 = 0 # 用于记录0的个数
        nums = [] # 用于存储没有0的其他数字
        # 遍历数组，统计0的个数，并得到一个没有0的数组nums
        for i in range(len(numbers)):
            if numbers[i] == 0:
                count_0 += 1
            else:
                nums.append(numbers[i])
        min_ = min(nums) #求取最小值
        max_ = max(nums) #求取最大值
        #最小值和最大值的差小于等于4，否则有0也没有用
        #若没有0，最大值与最小值的差应该正好为4，但是有0可以弥补一些，因此大于等于4-count_0
        if 4-count_0 <= max_ - min_ <= 4: 
            num = 1 # 用于统计数字的个数，到5则停止
            now = min_ + 1 # 当前数字
            while count_0 >=0 and num < 5:
                if now in nums: # 如果当前数字在数组中存在，num++， now++
                    num += 1
                    now += 1
                elif count_0 > 0: # 当前数字不存在数组，但是有0，可以用0代替一个
                    num += 1
                    now += 1
                    count_0 -= 1
                else: # 不在数组中，且没有0，就返回False
                    return False
            if num == 5: # num=5，说明有顺子
                return True
            return False
            