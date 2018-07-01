# 如果对于一个字符串A,将A的前面任意一部分挪到后面去形成的字符串称为A的旋转词。
# 比如A="12345",A的旋转词有"12345","23451","34512","45123","51234"。
# 对于两个字符串A和B,请判断A和B是否互为旋转词。
# 给定两个字符串A和B及他们的长度lena,lenb,请返回一个bool值,代表他们是否互为旋转词。
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True
# if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
# Note:
# - A and B will have length at most 100.


# 判断大字符串A+A中是否含有B
# Time:  O(n^2)
# Space: O(n)
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # if len(A) != len(B):
        #     return False
        # aa = A + A
        # if B in aa:
        #     return True
        # return False
        return len(A) == len(B) and B in A * 2


# 字符串的朴素匹配
# 可以想象成把文本串s固定住,模式串p从s最左边开始对齐,如果对齐的部分完全一样,则匹配成功,
# 失败则将模式串p整体往右移1位,继续检查对齐部分,如此反复.
class Solution2(object):
    def rotateString(self, s, p):
        if len(s) != len(p):
            return False
        ss = s + s
        m = len(ss)
        n = len(p)
        for i in range(m - n + 1):  # 起始指针i
            if ss[i:i + n] == p:
                return True
        return False


# Time:  O(n)
# Space: O(n)
# KMP algorithm
# 对模式串p进行预处理,得到前后缀的部分匹配表,使得我们可以借助已知信息,算出可以右移多少位.即 kmp = 朴素匹配 + 移动多位.
class Solution3(object):
    def kmp_match(self, s, p):   # "DABDABC"  "ABCDABD"
        if len(s) != len(p):
            return False
        ss = s + s             # "DABDABCDABDABC"
        table = self.partial_table(p)  # 得到模式串"ABCDABD"的部分匹配表  [0, 0, 0, 0, 1, 2, 0]
        print("table[-1]:", table[-1])
        cur = 0  # 起始指针cur
        while cur <= len(ss) - len(p):   # cur<=14-7
            for i in range(len(p)):      # i = 0 1 2 3 4 5 6
                if ss[i + cur] != p[i]:  # 当前元素不相等, 则向后移动
                    # 移动位数 = 已匹配的字符数 - 对应的部分匹配值
                    print("table[i-1]:", table[i-1])
                    cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                    break
            # for … else: else 中的语句会在循环正常执行完（即for不是通过break跳出而中断的）的情况下执行，
            # while … else 也是一样。
            else:
                return True
        return False

    # 部分匹配表
    def partial_table(self, p):
        '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
        prefix = set()
        postfix = set()
        ret = [0]   # 第一个字母 前缀后缀都为空集,共有元素长度为0
        for i in range(1, len(p)):
            # 遍历到第i个字母(从下标为1的第二个字母开始) :i 之前的前缀  i=1时 "AB" 前缀为"A"
            # 前缀是每次add新的 p[:i] 即为当前字符串的前缀集合
            prefix.add(p[:i])
            print("prefix:", prefix)
            # 后缀每次不同字符串,有不同的后缀集合  例:"ABC"的后缀为:"BC","C"
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            # prefix & postfix 表示前缀集合和后缀集合中的共有元素  如果没有共有元素 加上一个 or {''} 得到 {''} 否则返回set()
            # a = (prefix & postfix or {''}).pop() 得到共有元素的集合里的元素
            # len(a) 共有元素的长度
            print("postfix:", postfix)
            print("prefix & postfix or {''}:", prefix & postfix or {''})
            ret.append(len((prefix & postfix or {''}).pop()))
            print("result:", ret)
        return ret


# KMP
class Solution4(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def strStr(haystack, needle):
            def KMP(text, pattern):
                prefix = getPrefix(pattern)
                print(prefix)
                j = -1
                for i in range(len(text)):
                    while j > -1 and pattern[j + 1] != text[i]:
                        j = prefix[j]
                    if pattern[j + 1] == text[i]:
                        j += 1
                    if j == len(pattern) - 1:
                        return i - j
                return -1

            def getPrefix(pattern):
                prefix = [-1] * len(pattern)
                j = -1
                for i in range(1, len(pattern)):
                    while j > -1 and pattern[j + 1] != pattern[i]:
                        j = prefix[j]
                    if pattern[j + 1] == pattern[i]:
                        j += 1
                    prefix[i] = j
                return prefix

            if not needle:
                return 0
            return KMP(haystack, needle)

        if len(A) != len(B):
            return False
        return strStr(A*2, B) != -1


# Time:  O(n)
# Space: O(1)
# Rabin-Karp Algorithm (rolling hash)
class Solution5(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def check(index):
            return all(A[(i+index) % len(A)] == c
                       for i, c in enumerate(B))

        if len(A) != len(B):
            return False

        M, p = 10**9+7, 113
        p_inv = pow(p, M-2, M)

        b_hash, power = 0, 1
        for c in B:
            b_hash += power * ord(c)
            b_hash %= M
            power = (power*p) % M

        a_hash, power = 0, 1
        for i in range(len(B)):
            a_hash += power * ord(A[i%len(A)])
            a_hash %= M
            power = (power*p) % M

        if a_hash == b_hash and check(0): return True

        power = (power*p_inv) % M
        for i in range(len(B), 2*len(A)):
            a_hash = (a_hash-ord(A[(i-len(B))%len(A)])) * p_inv
            a_hash += power * ord(A[i%len(A)])
            a_hash %= M
            if a_hash == b_hash and check(i-len(B)+1):
                return True

        return False


if __name__ == '__main__':
    solution = Solution3()
    print(solution.partial_table("ABCDABD"))
    # print(solution.kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
    print(solution.kmp_match("DABDABC", "ABCDABD"))
