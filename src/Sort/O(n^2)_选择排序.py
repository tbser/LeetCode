# Time: O(n^2)

# 0 - N-1 选出一个最小值,放到第一个位置 (所有的数中选一个最小值)
# 1 - N-1 选出一个最小值,放到第二个位置 (除了第一个数, 所有后面的数中选一个最小值)
# ...


class Solution(object):
    def selectionSort(self, A):
        n = len(A)
        i = 0
        while i < n-1:
            min = i      # 假设最小值为当前数
            for j in range(i+1, n):  # 将所有后面的数 与当前数比较 找出最小值下标
                if A[j] < A[min]:
                    min = j

            if min != i:
                temp = A[i]
                A[i] = A[min]
                A[min] = temp

            i += 1

        return A


if __name__ == '__main__':
    print(Solution().selectionSort([2, 4, 7, 9, 8, 6]))
