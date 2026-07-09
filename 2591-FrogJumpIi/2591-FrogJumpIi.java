// Last updated: 7/9/2026, 9:01:30 AM
class Solution {
    public int maxJump(int[] stones) {
        int n = stones.length;
        int ans = 0;
        for (int i = 2; i < n; i++) {
            ans = Math.max(ans, stones[i] - stones[i - 2]);
        }
        ans = Math.max(ans, stones[n - 1] - stones[n - 2]);

        return ans;
    }
}
