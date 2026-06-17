class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            a = float('-inf') if i == 0 else A[i - 1]
            b = float('inf') if i == m else A[i]
            c = float('-inf') if j == 0 else B[j - 1]
            d = float('inf') if j == n else B[j]

            if a <= d and c <= b:
                if (m + n) % 2:
                    return max(a, c)
                return (max(a, c) + min(b, d)) / 2

            if a > d:
                r = i - 1
            else:
                l = i + 1
