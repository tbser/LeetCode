# coding:utf-8
# 字符串同构

# Time:  O(n)
# Space: O(1)

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Note:
# You may assume both s and t have the same length.

# 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

# 两个字符串是同构的充要条件是 它们之间相同位置的字符存在一一对应关系可以相互替换。
# 在字符串s中不存在两个不同的字符映射到t中同一个字符的情况，但一个字符可以映射到它自身。

from itertools import izip  # Generator version of zip.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True





