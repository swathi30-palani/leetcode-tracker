# Last updated: 7/9/2026, 9:03:29 AM
class Solution:
    def searchRange(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = findLeft()
        right = findRight()

        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]
