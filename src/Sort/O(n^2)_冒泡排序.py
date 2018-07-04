# Time: O(n^2)

# 0 - N-1 选出一个最小值,放到第一个位置 (所有的数中选一个最小值)
# 1 - N-1 选出一个最小值,放到第二个位置 (除了第一个数, 所有后面的数中选一个最小值)
# ...


def bubbleSort(self, A):
    n = len(A)
    flag = 0
    while n:
        for i in range(n - 1):  # 与后l-1个数比较
            if A[i] > A[i + 1]:  # 当前数和后面一个数比较, 大的话交换位置
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
                flag = 1
        if not flag:  # 没有交换过程,已经有序,直接结束循环
            break
        n -= 1
    return A


if __name__ == '__main__':
    print(Solution().bubbleSort([2, 4, 7, 9, 8, 6]))
    # print(Solution().bubbleSort([2, 4, 6, 7, 8, 9]))
