# Time: O(n^2)

# 从位置1开始，跟前面一个数（位置0）比较，如果位置1小，交换位置。
# 将位置2与位置1比较，如果位置2大，结束比较，如果位置2小，交换位置，再与位置0比较，如果位置0大交换位置。
# ...
# 对于当前需要排序的数, 向前一次交换, 直到前面的的数小于等于它,停止交换。


class Solution(object):
    def insertionSort(self, A):
        n = len(A)
        i = 1           # 从位置1开始

        while i < n:    # 需要遍历到最后一个数
            temp = A[i]
            j = i - 1    # 与前一个数比较

            while j >= 0 and A[j] > temp:   # 对于当前位置i 的一次比较过程
                A[j + 1] = A[j]  # 后移过程
                j -= 1           # 继续往前比较

            A[j + 1] = temp
            i += 1

        return A


if __name__ == '__main__':
    print(Solution().insertionSort([54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]))
