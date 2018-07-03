# Time: O(n^2)

# 0 - N-1 从第一个数往后依次比较,大的往后移, 最大的数到达最后一个位置
# 0 - N-2 第二大的数到达倒数第二个位置
# ...


class Solution(object):
    def bubbleSort(self, A):
        l = len(A)
        flag = 0
        while l:
            for i in range(l-1):   # 对前l-1个数遍历(除了最后一个数 前面的数)
                if A[i] > A[i+1]:  # 当前数和后面一个数比较, 大的话交换位置
                    temp = A[i]
                    A[i] = A[i+1]
                    A[i+1] = temp
                    flag = 1
            if not flag:   # 没有交换过程,已经有序,直接结束循环
                break
            l -= 1
        return A


if __name__ == '__main__':
    print(Solution().bubbleSort([2, 4, 7, 9, 8, 6]))
    # print(Solution().bubbleSort([2, 4, 6, 7, 8, 9]))
