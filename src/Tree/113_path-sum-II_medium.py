# coding:utf-8

# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.pathSumRecu([], [], root, sum)

    def pathSumRecu(self, result, cur, root, sum):
        if not root:
            return result

        if root.left is None and root.right is None and root.val == sum:
            print("cur:{}".format(cur))
            print("root.val:{}".format(root.val))
            print("cur+[root.val]:{}".format(cur+[root.val]))
            # print("cur.append(root.val):{}".format(cur.append(root.val)))  # None
            result.append(cur+[root.val])
            return result

        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, sum - root.val)
        self.pathSumRecu(result, cur, root.right, sum - root.val)
        a = cur.pop()
        print("a:{}".format(a))

        return result


class Solution2(object):
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        result = []
        self.dfs(root, sum, [], result)
        return result

    def dfs(self, root, sum, cur, result):
        if not root:
            return

        if root.left is None and root.right is None and sum==root.val:
            result.append(cur+[root.val])
            return

        self.dfs(root.left, sum-root.val, cur+[root.val], result)
        self.dfs(root.right, sum-root.val, cur+[root.val], result)


class Solution3(object):
    def pathSum(self, root, sum):
        return self.pathSumRecu(root, sum, [], [])

    def pathSumRecu(self, root, sum, cur, result):
        if not root:
            return result

        if root.left is None and root.right is None and root.val==sum:
            result.append(cur+[root.val])
            return result

        self.pathSumRecu(root.left, sum - root.val, cur+[root.val], result)
        self.pathSumRecu(root.right, sum - root.val, cur+[root.val], result)
        return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(1)
    print(Solution3().pathSum(root, 8))
