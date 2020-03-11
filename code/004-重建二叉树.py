# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
@题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

@解题思路
首先要理解什么是前序遍历，什么是中序遍历。
前序遍历：父节点，左节点，右节点
中序遍历：左节点，父节点，右节点
也就是，前和中这两个词都是相对于父节点来说的，父节点首先遍历就是前序遍历，父节点第二个遍历，就是中序遍历。

以一个例子作为说明：
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

前序遍历首先遍历父节点，中序遍历先遍历左节点，那么显然，pre[0]就是当前树的父节点，而中序遍历中tin[3]==1，我们用index表示父节点在中序遍历中所在的位置，即index=3，因此tin[0:index]这三个节点相对于父结点来说都是左节点，tin[4:]相对于父节点来说都是右节点，于是可以轻松地根据中序遍历将树分为左子树tin[0:3]，父节点tin[3]，右子树tin[4:]，左子树和右子树可继续递归。
同样的，可以根据前序遍历将树进行划分：父节点为pre[0]，那么可以知道index=左子树的节点数。于是可以将前序遍历分为左子树pre[1:index+1], 右子树pre[index+1:]

将前序遍历和中序遍历都划分为左右子树之后，就可以根据递归求解。

'''
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0: #当pre中不含结点时递归结束
            return None
        root = TreeNode(pre[0]) #获取父节点
        index = tin.index(pre[0]) #获取父节点在中序遍历中的索引位置
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])#
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root


'''
@测试代码
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
def print_tree(root):
    if root == None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

a = Solution()
root = a.reConstructBinaryTree(pre, tin)
print_tree(root)
'''