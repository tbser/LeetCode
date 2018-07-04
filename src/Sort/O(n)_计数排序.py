

class Solution(object):
    def countingSort(self, A):
        n = len(A)

        min = max = A[0]
        for i in range(1, n):
            if A[i] <= min:
                min = A[i]
            if A[i] > max:
                max = A[i]

        import collections
        counts = collections.defaultdict(int)

        for i in range(0, n):
            counts[A[i] - min] += 1

        j = 0
        for i in range(0, max - min + 1):
            while counts[i]:
                A[j] = i + min
                counts[i] -= 1
                j += 1

        return A


if __name__ == '__main__':
    print(Solution().countingSort([54, 35, 48, 36, 27, 12, 44, 44, 8, 14, 26, 17, 28]))
