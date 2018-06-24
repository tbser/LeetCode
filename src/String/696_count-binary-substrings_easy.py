# coding:utf-8
# 统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数

# Time:  O(n)
# Space: O(1)

# Give a string s, count the number of non-empty (contiguous) substrings
# that have the same number of 0's and 1's, and all the 0's and all the 1's
# in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
#              "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        preLen, curLen, result = 0, 1, 0
        # preLen:上一个数字的长度(如果当前为0, 前面1的长度)
        # curLen:当前数字的长度
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curLen += 1
            else:
                preLen = curLen
                curLen = 1
            # 只要上一个数字的长度 大于或者等于 当前数字的长度, 就算一个结果子串
            if preLen >= curLen:
                result += 1

        return result


class Solution2(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        result += min(prev, curr)
        return result