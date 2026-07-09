# Last updated: 7/9/2026, 9:04:00 AM
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if current is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match

        return closest_sum

# Example usage
sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(sol.threeSumClosest([0, 0, 0], 1))       # Output: 0
