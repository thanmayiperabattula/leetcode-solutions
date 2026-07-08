from collections import Counter
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        gp = 0
        for num in nums:
            counter[num] -= 1
            gp += counter[num]
        return gp

