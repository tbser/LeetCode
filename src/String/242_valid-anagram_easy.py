# coding:utf-8
# 两个字符串包含的字符是否完全相同
#
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# 字符串只包含小写字符，总共有 26 个小写字符。
# 可以用 Hash Table 来映射字符与出现次数，因为键值范围很小，
# 因此可以使用长度为 26 的整型数组对字符串出现的字符进行统计，
# 然后比较两个字符串出现的字符数量是否相同。


# Time:  O(n)
# Space: O(1)
import collections
import string


class Solution(object):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1

        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1
            if count[c.lower()] < 0:
                return False

        return True

    def isAnagram2(self, s, t):
        return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])

    def isAnagram3(self, s, t):
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True


# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


