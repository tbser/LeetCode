# coding:utf-8
# 对于一个有序数组 arr,再给定一个整数 num,请在 arr 中找到 num 这个数出现的最左边的位置。
# 给定一个数组 arr 及它的大小n,同时给定 num。请返回所求位置。若该元素在数组中未出现,请返回-1.

# example:
# input: [1,2,3,3,4], 5, 3
# output: 2


class Solution(object):
    def findPos(self, arr, n, num):
        res = -1
        if n == 0:
            return res

        low = 0 
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == num:
                res = mid
                high = mid - 1  # 继续搜索左边部分

            elif arr[mid] > num:
                high = mid - 1
            else:
                low = mid + 1
        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4]
    print(Solution().findPos(arr, 5, 3))
