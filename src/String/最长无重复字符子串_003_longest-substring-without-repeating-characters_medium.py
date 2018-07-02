# 给定一个字符串str，返回str的最长无重复字符子串的长度。
# 举例:
# str="abcd"，返回4.
# str="abcb"，最长无重复字符子串为"abc"，返回3.

# Given a string, find the length of the longest substring without repeating characters.

# Example:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
#
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# 最优解 Time: O(N) Space: O(N)
# 求出以str中每个字符结尾的情况下，最长无重复字符子串的长度，并在其中找出最大值返回。
#
# 哈希表map —> 其中统计了每种字符之前出现的位置
# 整型变量Pre -> 代表以s[i-1]结尾的情况下，最长无重复子串的长度。
# ---------------_c--------
#           s[i-1] s[i]


# Time:  O(N)
# Space: O(N)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if s is None:
            return res
        d = {}     # 借助一个辅助键值对 来存储 某个元素最后一次出现的下标。
        start = 0  # 用一个整形变量存储 当前 无重复字符的子串 开始的下标。

        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1

            d[s[i]] = i
            res = max(res, i - start + 1)
        return res


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, visited = 0, 0, [False for _ in range(256)]

        for index, c in enumerate(s):
            # ord() 函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，
            # 它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值
            if visited[ord(c)]:
                while c != s[start]:    # 当前字符和前面出现过的比较 如果不相等 设为False
                    visited[ord(s[start])] = False  # 当前字符与前面下标为start的字符比 不一样 则s[start]设为False
                    start += 1    # 前面需要比较的值 往后移一步
                # c和前面的字符一样 start同样需要往后移一位
                start += 1
            else:
                visited[ord(c)] = True

            longest = max(longest, index - start + 1)
        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # "abcabcbb" 3   pwwkew 3


