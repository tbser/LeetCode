# Time: O(n)
# Space:O(1)
#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?

# 先把每个字符都逆转: "eulb si yks eht",
# 然后把每个单词逆转: "blue is sky the"。

# 写一个reverse函数，依次分别从字符串的开头和结尾遍历，交换字符位置


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """

        def reverse(s, begin, end):
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        begin = 0
        for j in range(len(s) + 1):  # 0, 1, 2, ..., len(s)
            if j == len(s) or s[j] == ' ':   # 判断条件 不能调换位置
                reverse(s, begin, j)
                begin = j + 1


if __name__ == '__main__':
    s = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    Solution().reverseWords(s)
    print(s)
