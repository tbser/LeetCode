# coding:utf-8
# 判断是否是平衡二叉树（AVL树）

# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as：
#   a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 对于结点root来说，先遍历root的左子树，遍历的过程中收集两个信息：
# 1、root的左子树是否为平衡二叉树(true or false)->如果左子树为false，则直接返回false；
# 2、root的左子树最深到哪一层，LH

# 如果root的左子树是平衡二叉树，再去遍历root的右子树，遍历的过程中依然收集两个信息：
# 1、root的右子树是否为平衡二叉树(true or false)->如果root的右子树为false，则直接返回false；
# 2、root的右子树最深到哪一层，RH

# 如果root的左子树和右子树都是平衡二叉树，则比较LH和RH的差的绝对值是否大于1，如果大于1，则不是平衡二叉树；
# 如果不大于1，则返回LH和RH中较大的一个 作为以当前root为头的树的深度。
class Solution(object):
    # 递归判断每一棵子树是否满足，并把自己的高度返回
    # 每棵树平衡的定义是，左子树的高度和右子树的高度相差不超过1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(root):
            if not root:
                return 0   # 空树是平衡二叉树
            lh, rh = get_height(root.left), get_height(root.right)
            if lh < 0 or rh < 0 or abs(lh - rh) > 1:   # lh < 0 or rh < 0 只要任何一个地方不满足了，就要break
                return -1
            return max(lh, rh) + 1

        return (get_height(root)>=0)
