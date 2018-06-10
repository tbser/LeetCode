# coding:utf-8
# 判断一个整数是否是回文数

# Time:  O(1)
# Space: O(1)
#
# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
# Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
# 题目要求：不能使用额外空间，也就不能将整数转换为字符串进行判断。

# Example 1:
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.


# 将整数分成左右两部分，右边那部分需要转置，然后判断这两部分是否相等。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False

        right = 0
        while x > right:
            right = right * 10 + x % 10
            x //= 10

        return x == right or x == right//10   # 偶数位 or 奇数位


# 转置整个数
class Solution2(object):
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse = reverse * 10 + copy % 10
            copy //= 10

        return x == reverse


# 得到每个位置的数字
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False

        dig = {}
        count = 1
        while x != 0:
            right = x % 10
            dig[count] = right
            count += 1
            x //= 10

        r = count - 1
        l = 1
        while l < r:
            if dig[l] != dig[r]:
                return False
            else:
                l += 1
                r -= 1
        return True