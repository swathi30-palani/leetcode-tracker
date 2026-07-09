# Last updated: 7/9/2026, 9:03:06 AM
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
