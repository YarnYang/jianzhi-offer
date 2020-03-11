# -*- coding:utf-8 -*-
'''
@题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

@解题思路
把数字的字符串存入数组，字符对应的下标就是其整数表示。

具体实现看代码，更清晰。
'''
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        label = 1 # 用于标记数字是正数还是负数
        # 将所有数字对应的字符存入数组，字符的下标就是对应的数字
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 判断这个数是正数还是负数，+ - 只能出现在第一个字符。
        # 由于正数可以省略+号，因此不一定进入if语句，默认label为1
        if s[0] == '+' or s[0] == '-':
            label = 1 if s[0] == '+' else -1
            s = s[1:] # 若第一个符号为+/-，数字部分为s[1:]
        sum_ = 0
        # 对s中的每一个字符进行for循环
        for i in s:
            # 若当前字符在num_list中，则计算数字的大小
            if i in num_list:
                sum_ = sum_*10 + num_list.index(i)
            # 否则返回0，表示不是整数
            else:
                return 0
        # 判断数字是否移除，补码的表示方法可以表示[-2^32, 2^32-1]，超出这个返回则返回0
        if -0x80000000 <= sum_*label <= 0x7FFFFFFF:
            return sum_*label
        else:
            return 0
        
            