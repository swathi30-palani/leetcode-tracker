# Last updated: 7/9/2026, 9:03:31 AM
class Solution:
    def countAndSay(self, n):
        def rle(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        seq = "1"
        for _ in range(n - 1):
            seq = rle(seq)
        return seq
