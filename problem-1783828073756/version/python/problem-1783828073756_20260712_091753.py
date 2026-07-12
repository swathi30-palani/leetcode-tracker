# Last updated: 7/12/2026, 9:17:53 AM
1class Solution(object):
2    def minimumCost(self, nums, k):
3        MOD = 10 **9+7
4
5        resource = k
6        operations = 0
7        ans = 0
8
9        for x in nums:
10            if resource < x:
11                need = x - resource
12                add = (need + k - 1) // k
13
14                ans = (ans +(operations + 1 + operations + add) * add // 2) % MOD
15                operations += add
16                resource += add * k
17            resource -= x
18        return ans % MOD