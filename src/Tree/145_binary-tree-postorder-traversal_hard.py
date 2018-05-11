# coding:utf-8
# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# 方法一：使用两个栈实现
# 1、申请一个栈，记为s1，然后将头结点压入s1中。
# 2、从s1中弹出的结点记为cur，然后先把cur的左孩子压入s1中，然后把cur的右孩子压入s1中。
# 3、在整个过程中，每一个从s1中弹出的结点都放进第二个栈s2中。
# 4、不断重复步骤2和步骤3，直到s1为空，过程停止。
# 5、从s2中依次弹出结点并打印，打印的顺序就是后序遍历的顺序了。

# 不管是递归方法还是非递归方法，遍历整棵树的时间复杂度都是O(N)，N为二叉树的结点数，额外空间复杂度为O(L)，L为二叉树的层数。


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s1, s2, result = [], [], []
        cur = root
        if not cur:
            return []
        s1.append(cur)

        while len(s1) != 0:
            cur = s1.pop()
            s2.append(cur.val)
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s1.append(cur.right)

        for i in range(len(s2)):
            result.append(s2.pop())

        return result


# Morris Traversal Solution
class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [], dummy
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right

        return result

    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur is not to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution3(object):
    def postorderTraversal(self, root):
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
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return result