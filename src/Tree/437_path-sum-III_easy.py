# coding:utf-8
# 统计路径和等于一个数的路径数量

# Time:  O(n)
# Space: O(h)

# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 路径不一定以root开头，也不一定以leaf结尾，但是必须连续。
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        # 从当前root开始的路径　从root的左孩子、root右孩子开始的路径
        res = self.pathSumStartWithRoot(root, sum) + \
              self.pathSum(root.left, sum) + \
              self.pathSum(root.right, sum)

        return res

    # 从当前root结点开始
    def pathSumStartWithRoot(self, root, sum):
        if not root:
            return 0
        count = 0
        if root.val == sum:  # 该root本身的值就等于sum
            count += 1

        count += self.pathSumStartWithRoot(root.left, sum-root.val) + \
                 self.pathSumStartWithRoot(root.right, sum-root.val)

        return count


import collections


class Solution2(object):
    # 路径不一定以root开头，也不一定以leaf结尾，但是必须连续。
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, sum, curr, lookup):
            if root is None:
                return 0
            curr += root.val
            result = lookup[curr-sum] if curr-sum in lookup else 0
            lookup[curr] += 1
            result += pathSumHelper(root.left, sum, curr, lookup) + \
                      pathSumHelper(root.right, sum, curr, lookup)
            lookup[curr] -= 1
            if lookup[curr] == 0:
                del lookup[curr]
            return result

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return pathSumHelper(root, sum, 0, lookup)

