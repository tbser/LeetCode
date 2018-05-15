# coding:utf-8
# 完全二叉树  binary search

# Given a complete binary tree, count the number of nodes.
# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at
# the last level h.
# Example:
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# Output: 6


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 判断是否为完全二叉树：
# 1、采用按层遍历二叉树的方式，从每层的左边向右边依次遍历所有的结点。
# 2、如果当前结点有右孩子，但没有左孩子，直接返回false。
# 3、如果当前结点并不是左右孩子全有，那之后的结点必须都为叶节点，否则返回false。
# 4、遍历过程中如果不返回false，遍历结束后返回true即可。

# count完全二叉树的结点数：
# Time:  O(h^2) = O((logN)^2)    h = log(N+1)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 得到左子树和右子树的高度
        depthofleft = self.depthofComBitree(root.left)
        depthofright = self.depthofComBitree(root.right)
        # 如果相等，说明右子树的最左下结点到达了最后一层，说明头节点的左子树一定是一棵满的二叉树，可以根据公式直接算出
        # 左子树的结点个数。剩下的可以用递归的方法在右子树上求结点数。
        if depthofleft == depthofright:
            return 2**depthofleft + self.countNodes(root.right)
        # 如果头节点的右子树的最左下结点不能到达最后一层，说明头节点的右子树一定也是一棵满的二叉树，只不过是比左子树少
        # 一层，依然可以根据公式直接算出右子树的结点个数。剩下的可以用递归的方法在左子树上求结点数。
        else:
            return 2**depthofright + self.countNodes(root.left)

    def depthofComBitree(self, node):   # 遍历到当前子树的最左下结点
        if not node:
            return 0
        depth = 0
        cur = node
        while cur:
            depth += 1
            cur = cur.left
        return depth


# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)
class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        node = root
        level = 0
        while node.left:
            node = node.left
            level += 1

        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = left + (right - left) / 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1

        return left - 1

    # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2

        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None
