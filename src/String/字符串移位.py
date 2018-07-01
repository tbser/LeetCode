# coding:utf-8

# 给定一个字符串str，和一个整数i。i代表str中的位置，将str[0...i]移动右侧，str[i+1...N-1]移到左侧。

# eg: str="ABCDE", i=2  output: "DEABC". 要求时间复杂度为O(N), 额外空间复杂度为O(1)。

# 1、将str[0...i]部分的字符逆序   ABCDE -> CBADE
# 2、将str[i+1...N-1]部分的字符逆序  CBADE -> CBAED
# 3、将str整体的字符逆序  CBAED -> DEABC


class Solution(object):
    def translation(self, s, i):
        reversed_pre = s[:i+1][::-1]
        reversed_post = s[i+1:][::-1]
        word = reversed_pre + reversed_post

        return word[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.translation("ABCDE", 2))
