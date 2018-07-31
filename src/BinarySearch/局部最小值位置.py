# coding:utf-8
# 给定无序数组 arr, 已知 arr 中任意两个相邻的数都不相等,
# 写一个函数, 只需返回 arr 中任意一个局部最小出现的位置即可。
# Time: O(logN)


class Solution(object):
    def getLessIndex(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        
        if n == 1 or arr[0] < arr[1]:   # 数组第一个数比第二个数小,直接返回第一个数的下标0
            return 0

        if arr[n - 1] < arr[n - 2]:  # 数组最后一个数比倒数第二个数小,直接返回最后一个数下标 n-1
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = low + (high - low) // 2   # 更安全的写法,(low+high)可能会溢出。
            if arr[mid] > arr[mid - 1]:
                high = mid - 1
            elif arr[mid] > arr[mid + 1]:
                low = mid + 1
            else:
                return mid

        return -1


if __name__ == '__main__':
    arr = [10, 5, 10, 5, 0, 1, 2, 4, 7, 3, 2, 9, 5, 4, 6, 5, 10, 6, 7, 10, 9, 4, 3, 7, 2, 9, 5, 4, 6, 10]
    print(Solution().getLessIndex(arr))
