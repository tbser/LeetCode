# coding:utf-8

# 给定一个字符串类型的数组strs，同时给定它的大小,请找到一种拼接顺序，使得将所有字符串拼接起来组成的大字符串是所有可能性中字典顺序最小的，
# 并返回这个大字符串。

# eg：strs=["abc", "de"]。可以拼成"abcde"，也可以拼成"deabc"，但前者字典顺序更小，所以返回"abcde"。
#
# input: ["b", "ba"], 2。  output: "bab"
#
# 最优解的时间复杂度：O(N*logN),其实质是一种排序的实现:
# 如果str1+str2 < str2+str1，则str1放在前面，否则str2放在前面。


class Solution(object):
    def findSmallest(self, strs):
        self.quickSort(strs, 0, len(strs)-1)
        res = ""
        for i in range(len(strs)):
            res += strs[i]
        return res

    # 快排
    def quickSort(self, strs, low, high):
        if low < high:
            # 随机的在数组中选择一个数key, 小于等于key的数统一放到key的左边, 大于key的数统一放到key的右边。
            # 划分后 key的位置n:
            n = self.partition(strs, low, high)
            # 以key值划分好后的字符串 对key的左右两个部分,分别递归调用快排过程:
            self.quickSort(strs, low, n-1)
            self.quickSort(strs, n+1, high)

    # 快排的划分过程
    def partition(self, strs, low, high):
        # 选第一个元素为Key值
        key = strs[low]
        # 从右到左遍历所有元素
        while low < high:
            # strs[high]比Key大或者等于key, 位置不变, high往前移一位
            while low < high and self.LT(key, strs[high]):  # key放前面, 即key<=strs[high] Key的字典序小
                high -= 1
            # strs[high]比key小, 将strs[high]放到最左边的位置。
            strs[low] = strs[high]

            # strs[low]比Key小或者等于key, 位置不变, low往后移一位
            while low < high and self.LT(strs[low], key):  # strs[low]放前面, 即key>=strs[low]
                low += 1
            # strs[low]比Key大, 将strs[low]放到最右边的位置。
            strs[high] = strs[low]

        # 当遍历完所有元素,直到最后那个数(划分值)的时候,将划分值与小于等于区间的下一个元素交换。
        # 最后的Low (小于key的都放到了左边 low右移 大于Key的都放到了右边)  low所在位置为key应该放的位置
        strs[low] = key
        return low     # 返回Key的位置

    # 两两比较, 按字典序
    def LT(self, s1, s2):
        temp1 = s1 + s2
        temp2 = s2 + s1
        if temp1 <= temp2:   # s1放前面 s1的字典序小
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    strs = ["abc", "de", "cab"]
    strs1= ["b", "ba"]
    print(solution.findSmallest(strs1))
