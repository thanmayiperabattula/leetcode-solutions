from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Step 1: Count how many numbers fall into each digit-sum group
        z = Counter(sum(map(int, str(v))) for v in range(1, n + 1))
        
        # Step 2: Count how many groups have each size
        zz = Counter(z.values())
        
        # Step 3: Find the largest group size and return how many groups have that size
        largest_size = max(z.values())          # biggest group size
        return zz[largest_size]                 # how many groups have that size

