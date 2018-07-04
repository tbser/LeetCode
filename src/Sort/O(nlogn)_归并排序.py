# Time: O(nlogn)

# 让数组中每个数成为一个长度为1的有序区间
# 将相邻的有序区间合并成一个最大长度为2的有序区间
# 将相邻的有序区间合并成一个最大长度为4的有序区间
# 。。。
# 直到把所有数合并成一个有序区间,排序结束。


class Solution(object):
    def mergeSort(self, A):
        n = len(A)
        self.mSort(A, A, 0, n - 1)   # 需要传入两份原始数组
        return A

    def mSort(self, A, B, low, high):
        if low == high:        # 一直//2  最后到1//2==low
            B[low] = A[low]           # 此处的B为新数组C
        else:
            mid = (low + high) // 2
            C = [0] * 100            # 定义一个空数组
            self.mSort(A, C, low, mid)
            self.mSort(A, C, mid + 1, high)
            self.merge(C, B, low, mid, high)    # 此处的B为原始数组A

    def merge(self, A, B, low, mid, high):  # A中划分成左右两部分 比较大小 合并到B中
        i = low          # B的下标起始
        j = mid + 1
        while low <= mid and j <= high:
            if A[low] < A[j]:
                B[i] = A[low]  # 左边小的先放入B
                low += 1       # 左边下标右移一个
            else:
                B[i] = A[j]    # 右边小 放入B
                j += 1         # 右边下标右移一个
            i += 1         # B中的下一个位置

        if low <= mid:          # 左边部分 还剩元素 都直接按顺序放入B中
            while low <= mid:
                B[i] = A[low]
                i += 1
                low += 1

        if j <= high:           # 右边部分 还剩元素 都直接按顺序放入B中
            while j <= high:
                B[i] = A[j]
                i += 1
                j += 1


if __name__ == '__main__':
    print(Solution().mergeSort([54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]))
