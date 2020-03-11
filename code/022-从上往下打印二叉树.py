# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

@解题思路
用一个队列存储结点，依次打印队列中的值即可
'''
import Queue
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        q = Queue.Queue() # python2的queue用法，python3有所不同，其实可以直接用list
        q.put(root) # 初始化队列，把根节点put进来
        l = []
        while not q.empty():
            a = q.get() # 获取队列的头节点，打印
            l.append(a.val)
            if a.left != None: # 左节点不为空，put进队列
                q.put(a.left)
            if a.right != None: # 右节点不为空，put进队列
                q.put(a.right)
        return l 
        
        '''
        前序遍历
        if root == None:
            return root
        l = []
        l.extend([root.val])
        left = self.PrintFromTopToBottom(root.left)
        if left != None:
            l.extend(left)
        right = self.PrintFromTopToBottom(root.right)
        if right != None:
            l.extend(right)
        return l
        '''