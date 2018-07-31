# coding:utf-8
# 有一个有序数组 arr,其中不含有重复元素,请找到满足 arr[i] == i 条件的最左的位置。
# 如果所有位置上的数都不满足条件,返回-1.

# input: [-1,0,2,3], 4
# output: 2


class Solution(object):
    def findPos(self, arr):
        n = len(arr)
        res = -1

        if n == 0 or arr[0] > n - 1 or arr[n - 1] < 0:
            return res

        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < mid:
                low = mid + 1
            elif arr[mid] > mid:
                high = mid - 1
            else:
                res = mid
                high = mid - 1

        return res


if __name__ == '__main__':
    arr = [-1, 0, 2, 3]
    print(Solution().findPos(arr))
