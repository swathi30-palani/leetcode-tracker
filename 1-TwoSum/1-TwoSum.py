# Last updated: 7/9/2026, 9:04:29 AM
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

# --- Example usage ---
if __name__ == "__main__":
    # Test Input
    nums = [2, 7, 11, 15]
    target = 9

    # Create object and call method
    solution = Solution()
    result = solution.twoSum(nums, target)

    print("Output:", result)  # Should print: Output: [0, 1]num] = i