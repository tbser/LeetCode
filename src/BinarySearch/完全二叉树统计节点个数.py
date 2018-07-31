# coding:utf-8
# 给定一棵完全二叉树的根节点 root,返回这棵树的节点个数。
# 如果完全二叉树的节点数为 N,请实现时间复杂度低于 O(N)的解法。

# 遍历的方式时间复杂度为 O(N)
# 最优解: Time: log(N^2)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        depthOfLeft = self.depthOfComBitree(root.left)
        depthOfRight = self.depthOfComBitree(root.right)
        if depthOfLeft == depthOfRight:
            # 左子树和右子树高度一样,说明左子树肯定是满二叉树
            return pow(2, depthOfLeft) + self.countNodes(root.right)
        else:
            # 左子树和右子树高度不一样,说明右子树肯定是满二叉树
            return pow(2, depthOfRight) + self.countNodes(root.left)

    # 到二叉树最左下的节点, 得到二叉树高度
    def depthOfComBitree(self, root):
        if not root:
            return 0
        len = 0
        while root:
            len += 1
            root = root.left
        return len


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(2)
    print(Solution().countNodes(root))
