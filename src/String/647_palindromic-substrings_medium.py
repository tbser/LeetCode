# coding:utf-8
# 回文子字符串

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


# 从字符串的某一位开始，尝试着去扩展子字符串
class Solution(object):
    cnt = 0

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            self.extendSubstrings(s, i, i)     # 奇数长度
            self.extendSubstrings(s, i, i+1)   # 偶数长度
        return self.cnt

    def extendSubstrings(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            self.cnt += 1


# Manacher算法，时间复杂度O(n), 空间复杂度O(n)
# 该算法首先对字符串进行预处理，在字符串的每个字符前后都加入一个特殊符号，比如字符串 abcd 处理成 #a#b#c#d#,
# 为了避免处理越界，在字符串首尾加上不同的两个特殊字符(c类型的字符串尾部不用加，因为自带‘\0’)，
# 这样预处理后最终变成$#a#b#c#d#^，经过这样处理后有个好处是原来的偶数长度和奇数长度的回文在处理后的字符串中
# 都是奇数长度。假设处理后的字符串为s

# 对于已经预处理好的字符串,我们用数组p[i]来记录以字符s[i]为中心的最长回文子串向左/右扩张的长度（包括s[i]）,
# 以字符串“12212321”为例，p数组如下
# s：   $  #  1  #  2  #  2  #  1  #  2  #  3  #  2  #  1  #  ^
# p：      1  2  1  2  5  2  1  4  1  2  1  6  1  2  1  2  1
# 可以看出，P[i]-1正好是原字符串中回文串的总长度, 如果p数组已知，遍历p数组找到最大的p[i]就可以求出最长回文
# 的长度，也可以求出回文的位置
class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0] * len(s)
            C, R = 0, 0

            for i in range(1, len(s) - 1):
                i_mirror = 2*C-i
                if R > i:
                    P[i] = min(R-i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
            return P
        return sum((max_len+1)/2 for max_len in manacher(s))