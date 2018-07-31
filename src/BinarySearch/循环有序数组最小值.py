# coding:utf-8
# 对于一个有序循环数组 arr,返回 arr 中的最小值。
# 有序循环数组是指,有序数组左边任意长度的部分放到右边去,右边的部分拿到左边来。
# 比如数组 [1,2,3,3,4], 是有序循环数组, [4,1,2,3,3]也是。

# input：[4,1,2,3,3]
# output: 1


# class Solution(object):
#     def getMin(self, arr):
#         n = len(arr)
#         if n == 0:
#             return -1
#         if n == 1 or arr[0] < arr[n - 1]:   # 最左边的数小于最右边的数,就是正有序
#             return arr[0]
#
#         low = 0
#         high = n - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if arr[low] > arr[mid]:    # 如果最左边L的数大于mid, 肯定是循环调过来的部分,最小值肯定在L和mid之间,所以从左边部分继续搜索
#                 high = mid - 1
#             elif arr[mid] > arr[high]: # 如果mid大于最右边R的数, 最小值肯定在mid和R之间,所以从右边部分继续搜索
#                 low = mid + 1
#             else:                    # arr[low] <= arr[mid] and arr[high] >= arr[mid] and arr[low] >= arr[high]
#                                      # --> arr[low] = arr[high] = arr[mid]  用遍历的方式寻找最小值
#                 min = low
#                 for i in range(low + 1, high):
#                     if arr[i] < arr[min]:
#                         min = i
#                 return arr[min]
#
#         return -1


class Solution(object):
    def getMin(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        if n == 1 or arr[0] < arr[n - 1]:
            return arr[0]

        low = 0
        high = n - 1
        while low < high:
            mid = low + (high - low) // 2

            if arr[low] > arr[mid]:
                high = mid
            elif arr[mid] > arr[high]:
                low = mid + 1
            else:
                break

        if low == high:
            return arr[low]
        min = arr[low]
        while low <= high:
            if arr[low] < min:
                min = arr[low]
            low += 1
        return min


if __name__ == '__main__':
    arr = [4, 1, 2, 3, 3]
    print(Solution().getMin(arr))
