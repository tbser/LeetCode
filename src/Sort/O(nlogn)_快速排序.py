# Time: O(nlogn)

# 随机的在数组中选择一个数key, 小于等于key的数统一放到key的左边, 大于key的数统一放到key的右边。
# 对左右两个部分,分别递归的调用快速排序的过程。

# 快速排序——划分过程(Partition过程): 即找到一个数后,小于等于它的数如何放到它的左边,大于它的数如何放到它的右边。
# 1、令划分值放在整个数组最后的位置
# 2、设计一个小于等于区间,初始长度为0,放在 整个数组的左边
# 3、从左到右遍历所有元素,
#       如果当前元素m大于划分值,继续遍历下一个元素;
#       如果当前元素m小于等于划分值,将当前元素m和小于等于区间(在整个数组的左边)的下一个数进行交换。
#        令小于等于区间向右回一个位置(包含住刚刚那个元素m)。
#    ...
# 4、当遍历完所有元素,直到最后那个数(划分值)的时候,将划分值与小于等于区间的下一个元素交换。

# 这就是一个完整的划分过程,时间复杂度为 O(n)


class Solution(object):
    def qSort(self, strs):
        self.quickSort(strs, 0, len(strs)-1)
        return strs

    def quickSort(self, strs, low, high):
        if low < high:
            # 随机的在数组中选择一个数key, 小于等于key的数统一放到key的左边, 大于key的数统一放到key的右边。
            # 划分后 key的位置n:
            n = self.partition(strs, low, high)
            # 以key值划分好后的字符串 对key的左右两个部分,分别递归调用快排过程:
            self.quickSort(strs, low, n-1)
            self.quickSort(strs, n+1, high)

    # 划分过程
    def partition(self, strs, low, high):
        # 选第一个元素为Key值
        key = strs[low]
        # 从右到左遍历所有元素
        while low < high:
            # strs[high]比Key大或者等于key, 位置不变, high往前移一位
            while low < high and key <= strs[high]:
                high -= 1
            # strs[high]比key小, 将strs[high]放到最左边的位置。
            strs[low] = strs[high]

            # strs[low]比Key小或者等于key, 位置不变, low往后移一位
            while low < high and strs[low] <= key:
                low += 1
            # strs[low]比Key大, 将strs[low]放到最右边的位置。
            strs[high] = strs[low]

        # 当遍历完所有元素,直到最后那个数(划分值)的时候,将划分值与小于等于区间的下一个元素交换。
        # 最后的Low (小于key的都放到了左边 low右移 大于Key的都放到了右边)  low所在位置为key应该放的位置
        strs[low] = key
        return low     # 返回Key的位置


if __name__ == '__main__':
    solution = Solution()
    strs = [54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]
    print(solution.qSort(strs))



