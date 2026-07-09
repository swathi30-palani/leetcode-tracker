# Last updated: 7/9/2026, 9:03:20 AM
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Replace non-positive and out-of-range numbers with a placeholder (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Use index marking to flag presence of numbers 1 to n
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        # Step 3: Find the first index with a positive value
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If all indices are marked, the missing number is n + 1
        return n + 1
