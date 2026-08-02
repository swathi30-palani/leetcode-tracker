// Last updated: 8/2/2026, 8:53:12 AM
1class Solution {
2    public int countRatioSubarrays(int[] nums, int a, int b) {
3        int n = nums.length;
4        int ans = 0;
5        for(int i = 0; i < n; i++){
6            int even = 0;
7            int odd = 0;
8
9            for(int j = i; j < n; j++){
10                if((nums[j] & 1) == 0)
11                    even++;
12                else
13                    odd++;
14                if(odd > 0 && (long) even * b <= (long) odd  * a)
15                    ans++;
16            }
17        }
18        return ans;
19    }
20}