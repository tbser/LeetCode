# coding:utf-8
# 计算一组字符集合可以组成的回文字符串的最大长度

# Time:  O(n)
# Space: O(1)

# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
# Input: "abccccdd"
# Output: 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# 使用长度为 256 的整型数组来统计每个字符出现的个数，每个字符有偶数个可以用来构成回文字符串。
# 因为回文字符串最中间的那个字符可以单独出现，所以如果有单独的字符就把它放到最中间。


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        odds = 0
        for i in count:
            if count[i] % 2 != 0:
                odds += 1

        if odds==0:
            return slen
        else:
            return (slen-odds)+1
