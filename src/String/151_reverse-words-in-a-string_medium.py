# Time:  O(n)
# Space: O(n)
#
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Note:
# - A word is defined as a sequence of non-space characters.
# - Input string may contain leading or trailing spaces.
# However, your reversed string should not contain leading or trailing spaces.
# - You need to reduce multiple spaces between two words to a single space in the reversed string.
#


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = "the sky is  blue "
        # s.split() = ['the', 'sky', 'is', 'blue']

        # ' '.join(s.split) = "the sky is blue"  # 去掉多余空格

        # reversed(s.split()) => <list_reverseiterator object at 0x10b485048>
        # ' '.join(reversed(s.split())) = 'blue is sky the'

        return ' '.join(reversed(s.split()))


class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s.split()
        t.reverse()
        return ' '.join(t)


if __name__ == '__main__':
    print(Solution().reverseWords('hello world'))
