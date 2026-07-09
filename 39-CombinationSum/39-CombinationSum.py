# Last updated: 7/9/2026, 9:03:23 AM
class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # reuse same candidate
                path.pop()

        backtrack(0, [], 0)
        return result
