# 把数组中的N个数,建成一个大小为N的大根堆:
# 4 5 3 0 1 7 2 6
#         7
#      /    \
#     6      5
#    / \    / \
#   4   1  3   2
#  /
# 0
# 7 6 5 4 1 3 2 0

# 堆顶元素为所有元素中的最大值, 与堆的最后一个位置的数交换:
#         0
#      /    \
#     6      5
#    / \    / \
#   4   1  3   2
#  /
# 7
# 0 6 5 4 1 3 2 7

# 然后把最大值脱离整个堆结构,放到数组最后的位置,作为数组的有序部分:
#         0
#      /    \
#     6      5
#    / \    / \
#   4   1  3   2
# 0 6 5 4 1 3 2     7

# 把n-1个数的堆进行大根堆的调整:
#         6
#      /    \
#     4      5
#    / \    / \
#   0   1  3   2
# 6 4 5 0 1 3 2     7

# 交换:
#         2
#      /    \
#     4      5
#    / \    / \
#   0   1  3   6
# 2 4 5 0 1 3 6    7
#         2
#      /    \
#     4      5
#    / \    /
#   0   1  3
# 2 4 5 0 1 3    6 7

# 调整:
# ...


class Solution(object):
    def heapSort(self, A):
        n = len(A)

        # i = n // 2 - 1
        # while i >= 0:
        #     self.heapAdjust(A, i, n - 1)
        #     i -= 1
        for i in range(n//2 - 1, -1, -1):   # [n//2 -1, 0]  把当前N个数 调整成大根堆
            self.heapAdjust(A, i, n - 1)

        i = n - 1          # 最后一个数的下标 
        while i > 0:
            temp = A[0]     # 最后一个最小值和第一个最大值交换位置
            A[0] = A[i]
            A[i] = temp
            self.heapAdjust(A, 0, i - 1)  # 把除了最后一个最大值(i) 剩下的(i-1)继续调整成大根堆
            i -= 1

        return A

    def heapAdjust(self, A, start, end):  # 从下标s开始 到下标m 调整大根堆
        rc = A[start]

        left = 2 * start + 1    # 父节点s的左子结点 2*s+1
        while left <= end:
            right = left + 1
            if left < end and A[left] < A[right]:  # 右节点更大 所以left移到右节点的位置
                left = right

            if rc > A[left]:
                break

            A[start] = A[left]   # rc <= A[left]  把A[left]移到开始s的位置
            start = left         # left的位置为开始的位置
            left = 2 * left + 1   # 到当前节点的左子结点 2*i+1  继续比较左节点

        A[start] = rc


if __name__ == '__main__':
    print(Solution().heapSort([54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]))
