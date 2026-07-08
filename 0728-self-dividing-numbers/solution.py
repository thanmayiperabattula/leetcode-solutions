class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def snum(n: int) -> bool:
            count = 0

            for d in str(n):
                if int(d) != 0:
                    if n % int(d) == 0:
                        count += 1

            return count == len(str(n))

        res = []

        for i in range(left, right + 1):
            if snum(i):
                res.append(i)

        return res
