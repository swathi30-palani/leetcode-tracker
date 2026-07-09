# Last updated: 7/9/2026, 9:04:12 AM
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Height is the shorter line
            h = min(height[left], height[right])
            # Width is the distance between pointers
            w = right - left
            max_area = max(max_area, h * w)

            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
