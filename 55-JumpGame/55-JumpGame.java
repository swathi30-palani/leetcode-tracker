// Last updated: 7/9/2026, 9:02:54 AM
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false; 
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }
}
