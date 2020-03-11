# -*- coding:utf-8 -*-
'''
@题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

@解题思路
采用递归的方法。

分别两种情况，第二个字符为*和第二个字符不是*。

- 第二个字符不是*
若s[0] == pattern[0]，或者pattern[0] == '.'. 继续匹配后面的字符，否则返回False

- 第二个字符是*
又分为s[0] == pattern[0] 和 s[0] != patter[0]两种情况。
    - s[0] != patter[0]
    直接跳过pattern的两个字符，s不动

    - s[0] == pattern[0]
    可以分为三种情况，以下任一一种成立都可以
    1.pattern后移两个，s后移一个
    2.pattern原地不动，s后移一个
    3.pattern后移两个，s不动

具体细节看代码

'''
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # 循环跳出的条件，s和pattern都为0当然就是True
        if len(s) == 0 and len(pattern) == 0:
            return True
        # pattern已经遍历完，返回False
        elif len(s) > 0 and len(pattern) == 0:
            return False
        # s为0，pattern不为0，那就只有pattern第二个字符为*的可能，因此继续判断
        elif len(s) == 0 and len(pattern) > 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # 分为第二个字符为*或不为*的情况
        # 第二个字符是*：
        elif len(pattern) > 1 and pattern[1] == '*':
            #第一个字符不相等，pattern直接跳过两个字符
            if s[0] != pattern[0] and pattern[0] != '.':
                return self.match(s, pattern[2:])
            #第一个字符相等，有三种情况，任意情况符合都可
            #1.pattern后移两个，s后移一个
            #2.pattern原地不动，s后移一个
            #3.pattern后移两个，s不动
            else:
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern) or self.match(s[1:], pattern[2:])
        #第二个字符不为*: s[0] == pattern[0] 或者 pattern[0] == .
        else:
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[1:])
            else:
                return False
        
