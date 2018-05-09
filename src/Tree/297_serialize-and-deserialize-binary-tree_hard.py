# coding:utf-8
# 二叉树 序列化和反序列化

# Time:  O(n)
# Space: O(h)

# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can
# be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# For example, you may serialize the following tree
#
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1、假设序列化结果为str，初始时str为空字符串。
# 1、先序遍历二叉树时如果遇到空结点，在str末尾加上"#!"。
# 3、如果遇到不为空的结点，假设结点值为3，就在str的末尾加上"3!"。
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def serializeHelper(node):
            if not node:
                vals.append("#")
            else:
                vals.append(str(node.val))
                serializeHelper(node.left)
                serializeHelper(node.right)

        serializeHelper(root)
        return ' '.join(vals)  # vals=['1','#','2']    ' '.join(vals)='1 # 2'    '1'.join(vals)='11#12'

    #  str = "12!3!#!#!#!"
    #         |
    #  values = ["12","3","#","#","#"]
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def splitstr(data, sep):  # data: '1 # 2'   sep: ' '
            sepSize = len(sep)
            start = 0
            while True:
                idx = data.find(sep, start)    # '1 # 2'.find(' ', 0) = 1  下标
                if idx == -1:             # 到最后一个数字
                    yield data[start:]
                    return
                yield data[start:idx]
                start = idx + sepSize

        # vals = splitstr(data, ' ')    # Memory Limit Exceeded
        vals = iter(splitstr(data, ' '))

        def deserializeHelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializeHelper()
                node.right = deserializeHelper()
                return node

        return deserializeHelper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
