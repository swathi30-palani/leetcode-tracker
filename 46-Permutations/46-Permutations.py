# Last updated: 7/9/2026, 9:03:10 AM
class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return result
