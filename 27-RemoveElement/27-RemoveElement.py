# Last updated: 7/9/2026, 9:03:41 AM
class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer for the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
