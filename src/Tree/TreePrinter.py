# coding:utf-8
# 有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。
# 给定二叉树的根结点root，请返回打印结果，结果按照 每一层一个数组 进行储存，所有数组的顺序按照层数从上往下，且每一层的数组内元素按照
# 从左往右排列。保证结点数小于等于500.
# input:
#      1
#     / \
#    2  3
#   /  / \
#  4  5  6
#    / \
#   7  8
#
# output:
# 1
# 2 3
# 4 5 6
# 7 8


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树按层遍历  宽度优先遍历，队列结构
class TreePrinter(object):
    def printTree(self, root):
        import queue
        q = queue.Queue()
        q.put(root)
        last = root
        nlast = TreeNode(0)
        result, temp = [], []

        while not q.empty():
            curr = q.get()
            print(curr.val)
            temp.append(curr.val)
            if curr.left:
                q.put(curr.left)
                nlast = curr.left
            if curr.right:
                q.put(curr.right)
                nlast = curr.right
            if curr == last:
                result.append(temp)   # 每一层一个数组
                temp = []
                print('\n')
                last = nlast
        return result

