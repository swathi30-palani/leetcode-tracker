# Last updated: 7/9/2026, 9:03:40 AM
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        