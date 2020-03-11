# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

@解题思路
递归求解，对于root结点来说，左节点就是左子树，右节点就是右子树，因此只需递归即可。
由于没有新建结点，因此root还是root，是中间结点，最后因为返回表头，找到最左边的结点返回。
'''
class Solution:
    p = None
    def ConverHelp(self, cur):
        if cur == None:
            return
        # 找到左节点，结果会存在p中
        self.ConverHelp(cur.left)
        # 当前结点的左节点=p
        cur.left = self.p
        # 如果p不为空，p的右节点为当前结点
        if self.p:
            self.p.right = cur
        # 更新p为当前节点
        self.p = cur
        self.ConverHelp(cur.right)

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        self.ConverHelp(pRootOfTree)
        res = pRootOfTree
        # 找到最左边的结点作为表头返回
        while (res.left != None):
            res = res.left
        return res