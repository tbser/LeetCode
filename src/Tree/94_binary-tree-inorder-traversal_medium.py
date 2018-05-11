# coding:utf-8
# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# 1、申请一个新的栈，记为stack，申请一个变量cur，初始时令cur等于头节点。
# 2、先把cur结点压入栈中，对以cur结点为头的整棵子树来说，依次把整棵树的左边界压入栈中，即不断令cur=cur.left，然后重复步骤2.
# 3、不断重复步骤2，直到发现cur为空，此时从stack中弹出一个结点，记为node。打印node的值，并让cur=cur.right，然后继续重复步骤2.
# 4、当stack为空并且cur为空时，整个过程结束。

# 不管是递归方法还是非递归方法，遍历整棵树的时间复杂度都是O(N)，N为二叉树的结点数，额外空间复杂度为O(L)，L为二叉树的层数。


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        cur = root
        if not cur:
            return result
        stack.append(cur)

        while len(stack) != 0:
            # 把当前结点的所有左子树压入栈
            while cur.left:
                stack.append(cur.left)
                cur = cur.left

            # 到了最左边的叶子结点，叶子结点的左孩子为空，pop出的结点记为node，并print
            node = stack.pop()
            result.append(node.val)

            # 看pop出的结点的右孩子是否为空，不为空的话，压入栈中，并且cur结点为这个右孩子
            if node.right:
                stack.append(node.right)
                cur = node.right
            # 然后继续 重复 把所有左子树压入栈

        return result


# Morris Traversal Solution
class Solution2(object):
    def inorderTraversal(self, root):
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
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution3(object):
    def inorderTraversal(self, root):
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
                stack.append((root, True))
                stack.append((root.left, False))
        return result
