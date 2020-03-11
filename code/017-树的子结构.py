# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
''' 
@题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

@解题思路
如果当前结点相等，则判断两棵树是否相同。
若当前结点不相等，分别判断A的左子树和右子树与B是否相同。递归解决。

具体看注释。
'''
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val: #如果当前结点相同，判断两个树是否相同
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            # 如果result=False，也就是当前结点不相同或两棵树不相同，判断proot1的左右子树与proot2是否相同
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    
    def DoesTree1HasTree2(self, tree1, tree2):
        # tree2是子树
        # tree2已经遍历完了，返回True
        if tree2 == None:
            return True
        # 如果tree1已经遍历完了，tree2还没有，返回False
        if tree1 == None:
            return False
        # 如果tree1，tree2不相等，返回False
        if tree1.val != tree2.val:
            return False
        #继续判断tree1，tree2的左右子树是否相等
        return self.DoesTree1HasTree2(tree1.left, tree2.left) and self.DoesTree1HasTree2(tree1.right, tree2.right)
        
        
        