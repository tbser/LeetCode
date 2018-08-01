# coding:utf-8
# 如何更快的求一个整数 k 的 n 次方。
# 如果两个整数相乘并得到结果的时间复杂度维 O(1),得到整数 k 的 N 次方的过程请实现时间复杂度为 O(logN)的方法。
# 给定 k 和 n,请返回 k 的 n 次方,为了防止溢出,请返回结果 Mod 1000000007的值。
# input: 2,3
# output: 8

# 用 N 的二进制形式

# example:

# 10 ^ 75 = 10 ^ 1001011
#         = 10^64 * 10^8 * 10^2 * 10^1
#         = 10^1000000 * 10^1000 * 10^10 * 10^1

#   10^64 10^32 10^16 10^8 10^4 10^2 10^1
#      1    0     0     1    0    1    1


# Time: O(logN)
class QuickPower(object):
    def getPower(self, k, N):
        if k == 0:
            return 0
        if N == 0:
            return 1

        if k > 1000000007:
            k %= 1000000007

        arr, bit = [], []
        while N:
            # print("N:", N)
            arr.append(k)
            # print("arr:", arr)
            k *= k
            if k > 1000000007:
                k %= 1000000007

            if N % 2:
                bit.append(1)
            else:
                bit.append(0)

            # print("bit:", bit)
            N //= 2

        res = 1
        for i in range(0, len(bit)):
            if bit[i]:
                res *= arr[i]
                if res > 1000000007:
                    res %= 1000000007

        return res % 1000000007


if __name__ == '__main__':
    print(QuickPower().getPower(2, 4))
