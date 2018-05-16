# coding:utf-8
# 翻转树

# Time:  O(n)
# Space: O(h)
#
# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#

# Time:  O(n)
# Space: O(w), w is the max number of the nodes of the levels.

# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time:  O(n)
# Space: O(h)
# DFS, Recursive solution.
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root



# BFS solution.
import collections
class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class Solution2:
    def invertTree(self, root):
        if root:
            nodes = Queue()
            nodes.push(root)
            while not nodes.empty():
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.push(node.left)
                if node.right is not None:
                    nodes.push(node.right)

        return root


# Time:  O(n)
# Space: O(h)
# Stack solution.
class Solution3:
    def invertTree(self, root):
        if root:
            nodes = []
            nodes.append(root)
            while nodes:
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        return root
