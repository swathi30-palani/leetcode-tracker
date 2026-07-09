# Last updated: 7/9/2026, 9:04:23 AM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    median = (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    median = float(min(right1, right2))
                # \U0001f3af Return median formatted to 5 decimal places
                return float("{:.5f}".format(median))
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1