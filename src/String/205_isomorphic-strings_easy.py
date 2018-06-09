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

    
import collections
class Solution3(object):
    # 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。
    def isIsomorphic(self, s, t):
        preIndexOfS = collections.defaultdict(int)  # 直接{}的话，会有keyerror
        preIndexOfT = collections.defaultdict(int)  # preIndexOfT[key] 默认值为0

        for i in range(len(s)):
            if preIndexOfS[s[i]] != preIndexOfT[t[i]]:
                return False
            preIndexOfS[s[i]] = i + 1
            preIndexOfT[t[i]] = i + 1

        return True

# 这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，
# 但是values的类型，是function_factory的类实例，而且具有默认值。
# 比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key,
# d[key] 也有一个默认值，这个默认值是int()的默认值0.

# defaultdict属于内建函数dict的一个子类，调用工厂函数提供缺失的值。
