# 给定一个字符串str，判断是不是整体有效的括号字符串。
# 举例：
# str="()",返回true。str="(()())"，返回true。
# str="(())"，返回true。
# str="())"，返回false。str="()a()"，返回false。
#
# 最优解 Time: O(N) Space: O(1)
# 1、整型变量num，代表"("出现次数与")"出现次数的差值。
# 2、遍历的过程中如果遇到"("则num++。
# 3、遍历的过程中如果遇到")"则num--。
# 4、遍历的过程中如果num<0，说明右括号多于左括号，则直接返回false。
# 5、如果一直没有出现情况4，则一直遍历下去。
# 6、遍历完成后，如果num==0，则返回true，否则返回false。


class Solution(object):
    def checkValidString(self, s):
        num = 0
        for i in range(len(s)):
            if num < 0:      # 遍历的过程中如果num<0，说明右括号多于左括号，则直接返回false
                return False
            if s[i] == "(":
                num += 1
            if s[i] == ")":
                num -= 1
            if num == 0 and i != len(s)-1:    # ()() False
                return False
        if num == 0:
            return True
        return False


# Time:  O(n)
# Space: O(1)

# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:
# 1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.
#
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].


class Solution2(object):
    def checkValidString(self, s):
        lower, upper = 0, 0      # keep lower bound and upper bound of '(' counts
        # upper只有在出现右括号")"的时候 才- 否则一直+
        #   即 出现"("和其他字符的时候 upper一直增加 表示可以出现的")"个数  出现一个")"就-1
        # lower只有在出现左括号"("的时候 才+ 否则一直-
        #   即 出现")"和其他字符的时候 lower一直减少 表示已经被配对好的 给去掉
        for c in s:
            if c == "(":
                lower += 1
                upper += 1
            elif c == ")":
                lower -= 1
                upper -= 1
            else:
                lower -= 1
                upper += 1

            if upper < 0:
                break
            lower = max(lower, 0)

        return lower == 0


class Solution3(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower, upper = 0, 0  # keep lower bound and upper bound of '(' counts

        for c in s:
            lower += 1 if c == '(' else -1
            print("lower:", lower)
            upper -= 1 if c == ')' else -1
            print("uppper:", upper)
            print("\n")
            if upper < 0:
                break   # 如果upper小于0, 退出循环
            lower = max(lower, 0)

        return lower == 0  # range of '(' count is valid


if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution2()
    # print(solution.checkValidString(""))  # "()()" False   "(()())" True   "()a()" False  "" True
    print(solution2.checkValidString("((**)"))
    # ")("  False
    # "(((******))" True
    # "(())((())()()(*)(*()(())())())()()((()())((()))(*" False
