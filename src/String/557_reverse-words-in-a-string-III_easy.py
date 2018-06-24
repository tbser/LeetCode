# coding:utf-8
# 将每个单词逆序，保持该单词在句子中的位置不变

# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and
# there will not be any extra space in the string.


# 速度快
class Solution(object):
    def reverseWords(self, s):
        # word = 'huang'
        # reversed_word = word[::-1]  # 'gnauh'
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)

# 稍慢
# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s, begin, end):
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        s = list(s)
        begin = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, begin, j)
                begin = j + 1
        return "".join(s)

