# 给定一个字符串str，将其中所有空格字符替换成"%20"，假设str后面有足够的空间。
# a b c足够的空间
# 遍历str，发现空格数量为2，所以str在替换后，长度为5+2*2=9
# 所以从下标为8的位置开始拷贝
# a b c_ _ _ _
# a b c_ _ _ c


class Solution(object):
    def replaceSpace(self, str):
        s = str.split()
        return "%20".join(s)


class Solution2(object):
    def replaceSpace(self, str):
        num = 0
        for c in str:
            if c == " ":
                num += 1

        newLength = len(str) + num*2
        res = [0] * newLength
        j = newLength - 1
        i = len(str) - 1
        while j >= 0:
            if str[i] != " ":
                res[j] = str[i]
                j -= 1
                i -= 1
            else:
                res[j] = "0"
                j -= 1
                res[j] = '2'
                j -= 1
                res[j] = "%"
                j -= 1
                i -= 1

        return ''.join(res)


if __name__ == '__main__':
    solution = Solution2()
    print(solution.replaceSpace("a b c"))
