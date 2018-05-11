# coding:utf-8
# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# 1、首先申请一个新的栈，记为stack
# 2、然后将头结点root压入stack中。
# 3、每次从stack中弹出栈顶结点，记为cur，然后打印cur结点的值。如果cur右孩子不为空的话，将cur的右孩子先压入stack中。
#   最后如果cur的左孩子不为空的话，将cur的左孩子压入stack中。
# 4、不断重复步骤3，直到stack为空，全部过程结束。

# 不管是递归方法还是非递归方法，遍历整棵树的时间复杂度都是O(N)，N为二叉树的结点数，额外空间复杂度为O(L)，L为二叉树的层数。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        if not root:
            return result    # if input=[]  output []
        stack.append(root)

        while len(stack) != 0:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return result


# Morris Traversal Solution
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    result.append(curr.val)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution3(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
        return result






