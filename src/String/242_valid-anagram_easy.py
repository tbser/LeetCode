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

    # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
    # 元素除了是 0、空、FALSE 外都算 TRUE。
    # >>> all(['a', 'b', '', 'd'])  # 列表list，存在一个为空的元素
    # False
    # >>> all([0, 1，2, 3])  # 列表list，存在一个为0的元素
    # False
    # >>> all([])  # 空列表
    # True
    # >>> all(())  # 空元组
    # True
    def isAnagram2(self, s, t):
        # str.count(s)  返回字符串s在str中出现的次数
        # string.ascii_lowercase  小写字母’abcdefghijklmnopqrstuvwxyz’
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

# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，
# 而不是在原来的基础上进行的操作。
