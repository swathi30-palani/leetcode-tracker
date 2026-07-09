# Last updated: 7/9/2026, 9:03:21 AM
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # Skip duplicates
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # Move to next index
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return result
