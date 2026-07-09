# Last updated: 7/9/2026, 9:04:07 AM
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for word in strs[1:]:
            # Reduce the prefix until it matches the start of the word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

# Example usage
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
