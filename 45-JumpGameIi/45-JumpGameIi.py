# Last updated: 7/9/2026, 9:03:13 AM
class Solution:
    def jump(self, nums):
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
